FROM python:3.10
WORKDIR /code
COPY . .
RUN chmod +x utils/geckodriver
RUN chmod +x main.py
RUN pip install -r requirements.txt
CMD ["python3.10", "main.py"]

