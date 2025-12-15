FROM python:3.9-slim-buster

WORKDIR /app

COPY Order_Service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Order_Service/. .

EXPOSE 5001

CMD ["python", "app.py"]