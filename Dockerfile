FROM python:slim

WORKDIR /app

COPY app.py .

RUN pip install fastapi[all] uvicorn google-genai python-dotenv

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]