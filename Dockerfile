FROM python:3.11.0-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
# CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]