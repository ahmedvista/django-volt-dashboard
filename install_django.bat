py -m venv env
.\env\Scripts\pip install -r app\config\requirements.txt
.\env\Scripts\python app\manage.py makemigrations   
.\env\Scripts\python app\manage.py migrate   


set DJANGO_SUPERUSER_USERNAME=ahmed
set DJANGO_SUPERUSER_PASSWORD=Av123456
set DJANGO_SUPERUSER_EMAIL=ahmed@ahmed.com

.\env\Scripts\python app\manage.py createsuperuser --noinput  
@REM .\env\Scripts\python app\manage.py changepassword %DJANGO_SUPERUSER_USERNAME%


@REM .\env\Scripts\python app\manage.py runserver