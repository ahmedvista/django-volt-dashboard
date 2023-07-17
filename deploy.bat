@echo off
cls

set "host_ip=107.174.249.53"
set "host_user=root"
set "deploy_path=/var/www/test"
set "ssh_key="C:\Users\Ahmed\id_vscode""


@REM echo "delete old files except"
@REM ssh -i %ssh_key% %host_user%@%host_ip% "cd %deploy_path% && ls | grep -xv "db.sqlite3" | xargs sudo rm -rf"

py -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
py -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

@REM scp -rp -i %ssh_key% "app/*" %host_user%@%host_ip%:%deploy_path%
echo yes | .\cwrsync\bin\rsync.exe -avzu -e 'cwrsync\bin\ssh.exe -i %ssh_key%' "app/" %host_user%@%host_ip%:%deploy_path%/

@REM ssh -i %ssh_key% %host_user%@%host_ip% 'python3 -m venv %deploy_path%/env'
@REM ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/env/bin/pip install -r %deploy_path%/config/requirements.txt "
@REM ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/env/bin/python3 %deploy_path%/manage.py migrate --run-syncdb"

@REM echo ssh -i %ssh_key% %host_user%@%host_ip% 'python3 -m venv %deploy_path%/env'
@REM echo ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/env/bin/pip install -r %deploy_path%/config/requirements.txt "
@REM echo ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/env/bin/python3 %deploy_path%/manage.py migrate --run-syncdb"


@REM pause
@REM exit