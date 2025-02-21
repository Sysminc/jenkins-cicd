# Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
COPY . /app/unit-test
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
