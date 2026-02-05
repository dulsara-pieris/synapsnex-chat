FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install curl so your Python code can fetch ASCII
RUN apt-get update && apt-get install -y curl

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "client.py"]