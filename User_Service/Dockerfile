FROM python:3.9-slim-buster

WORKDIR /app

COPY User_Service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY User_Service/. .

EXPOSE 5000

CMD ["python", "app.py"]