@echo off
cls

set "host_ip=107.174.249.53"
set "host_user=root"
set "deploy_path=/var/www/smartkits_admin"
set "ssh_key="C:\Users\Ahmed\id_vscode""

@REM @REM echo "delete old files except"
@REM @REM ssh -i %ssh_key% %host_user%@%host_ip% "cd %deploy_path% && ls | grep -xv "db.sqlite3" | xargs sudo rm -rf"

py -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
py -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

@REM @REM scp -rp -i %ssh_key% "app/*" %host_user%@%host_ip%:%deploy_path%
echo yes | .\cwrsync\bin\rsync.exe -avzu -e 'cwrsync\bin\ssh.exe -i %ssh_key%' "app/" %host_user%@%host_ip%:%deploy_path%/

ssh -i %ssh_key% %host_user%@%host_ip% "sudo rm -rf %deploy_path%/env"
ssh -i %ssh_key% %host_user%@%host_ip% "python3.8 -m venv %deploy_path%/env"
ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/env/bin/pip3.8 install -r %deploy_path%/config/requirements.txt "
ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/env/bin/python3.8 %deploy_path%/manage.py migrate"
ssh -i %ssh_key% %host_user%@%host_ip% "sudo rm -rf %deploy_path%/staticfiles"
ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/env/bin/python3.8 %deploy_path%/manage.py collectstatic --noinput"

ssh -i %ssh_key% %host_user%@%host_ip% "sudo chown -R www-data:www-data %deploy_path%/*"
ssh -i %ssh_key% %host_user%@%host_ip% "chmod -R 777 %deploy_path%/"

scp -Cp -i %ssh_key% "app/config/deploy_files/smartkits.service" %host_user%@%host_ip%:/root/systemd/smartkits.service
scp -Cp -i %ssh_key% "app/config/deploy_files/smartkits.socket" %host_user%@%host_ip%:/root/systemd/smartkits.socket
ssh -i %ssh_key% %host_user%@%host_ip% "sudo systemctl daemon-reload"

ssh -i %ssh_key% %host_user%@%host_ip% "sudo systemctl restart smartkits.service"
ssh -i %ssh_key% %host_user%@%host_ip% "sudo systemctl enable smartkits.service"
ssh -i %ssh_key% %host_user%@%host_ip% "sudo systemctl restart smartkits.socket"
ssh -i %ssh_key% %host_user%@%host_ip% "sudo systemctl enable smartkits.socket"

@REM scp -rp -i %ssh_key% "app/config/deploy_files/nginx/smartkits" %host_user%@%host_ip%:/root/nginx/sites-available/smartkits
ssh -i %ssh_key% %host_user%@%host_ip% "ln -s /root/nginx/sites-available/smartkits /root/nginx/sites-enabled"
ssh -i %ssh_key% %host_user%@%host_ip% "sudo nginx -t ; sudo systemctl restart nginx"

@REM pause
exit

@REM python manage.py check --deploy