import os
import pathlib
import paramiko

hostname = "107.174.249.53"
port = 22
username = "root"
identity_file = r"C:\Users\Ahmed\id_vscode"
module_name = "smartkits"
deploy_path = rf"/var/www/{module_name}_admin"


def ssh_connection(hostname, port, username, identity_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file(identity_file)
    ssh.connect(hostname, port, username, pkey=private_key)
    return ssh


def run_remote_command(command):
    print(command)
    ssh = ssh_connection(hostname, port, username, identity_file)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read().decode().strip()
    err = stderr.read().decode().strip()
    if out:
        print(out)
    if err:
        print(err)
    ssh.close()
    return out


def prompt_yes():
    while True:
        user_input = input("Do you want to fast deploy? (y/n): ").strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            return True


def deploy():
    yes = prompt_yes()

    [p.unlink() for p in pathlib.Path(".").rglob("*.py[co]")]
    [p.rmdir() for p in pathlib.Path(".").rglob("__pycache__")]
    os.system(
        rf".\cwrsync\bin\rsync.exe -rvz -e 'cwrsync\bin\ssh.exe -i \'{identity_file}\'' app/ {username}@{hostname}:{deploy_path}/"
    )
    try:
        if not yes:
            run_remote_command(f"sudo rm -rf {deploy_path}/env")
            run_remote_command(f"python3.8 -m venv {deploy_path}/env")
            run_remote_command(f"{deploy_path}/env/bin/pip3.8 install -r {deploy_path}/config/requirements.txt")
            run_remote_command(f"cd {deploy_path} ; {deploy_path}/env/bin/python3.8 {deploy_path}/manage.py migrate")
            run_remote_command(f"sudo rm -rf {deploy_path}/staticfiles")
            run_remote_command(f"{deploy_path}/env/bin/python3.8 {deploy_path}/manage.py collectstatic --noinput")
            os.system(
                f'scp -Cp -i "{identity_file}" app/config/deploy_files/{module_name}.service {username}@{hostname}:/root/systemd/'
            )
            os.system(
                f'scp -Cp -i "{identity_file}" app/config/deploy_files/{module_name}.socket {username}@{hostname}:/root/systemd/'
            )
            run_remote_command(f"sudo systemctl daemon-reload; sleep 1")
            # os.system(
            #     f'scp -Cp -i "{identity_file}" app/config/deploy_files/nginx/smartkits {username}@{hostname}:/root/nginx/sites-available/'
            # )
            # run_remote_command(f"ln -s /root/nginx/sites-available/{module_name} /root/nginx/sites-enabled")
            run_remote_command(f"sudo systemctl enable {module_name}.service")
            run_remote_command(f"sudo systemctl enable {module_name}.socket")

        run_remote_command(f"sudo chown -R www-data:www-data {deploy_path}/*")
        run_remote_command(f"sudo chmod -R 777 {deploy_path}/")

        run_remote_command(f"sudo systemctl restart {module_name}.service")
        run_remote_command(f"sudo systemctl restart {module_name}.socket")
        run_remote_command(f"sudo nginx -t ; sudo systemctl restart nginx")

    except Exception as e:
        print("Error:", e)
