python manage.py migrate personas zero
python manage.py migrate Lugares zero
python manage.py migrate User zero
python manage.py makemigrations
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 my_first_project.wsgi:application