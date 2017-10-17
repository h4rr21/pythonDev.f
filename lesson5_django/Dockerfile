FROM python:2.7
COPY my_first_project/requirements.txt /my_first_project/requirements.txt
RUN pip install -r /my_first_project/requirements.txt
WORKDIR /my_first_project
COPY my_first_project /my_first_project
RUN pip install requests
CMD sh migrations.sh