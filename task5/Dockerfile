FROM python:3.7.9-buster

WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app

EXPOSE 9002

CMD ["python", "app/main.py"]