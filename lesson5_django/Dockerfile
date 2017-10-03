FROM python:2.7
WORKDIR /my_first_project
COPY my_first_project/requirements.txt my_first_project/requirements.txt
RUN pip install -r requirements.txt
COPY my_first_project /my_first_project
CMD gunicorn --bind 0.0.0.0:8000 my_first_project.wsgi:application

