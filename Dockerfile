FROM python:3.11

COPY . /code

RUN chmod +x code/utils/geckodriver
  
RUN pip install -r code/requirements.txt
RUN code/main.py

