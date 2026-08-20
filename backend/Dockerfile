FROM python:slim

WORKDIR /app

COPY app.py .

RUN pip install fastapi[all] uvicorn google-genai python-dotenv elasticsearch==8.12.0

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]