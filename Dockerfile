FROM python:3.11-slim

WORKDIR /app

COPY embedding_caller.py .

RUN pip install requests

CMD ["python", "embedding_caller.py"]
