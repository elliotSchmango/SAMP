#use small image
FROM python:3.11-slim

#set working directory
WORKDIR /app

#copy requirements/ install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]