
FROM python:3.12-slim

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt

RUN python -m pip install --no-cache-dir -r /app/requirements.txt

COPY app/ /app/

EXPOSE 5000

CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:5001", "app:app"]


