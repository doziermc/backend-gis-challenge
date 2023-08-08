FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

# install deps and repo
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "calculate_properties.main:app", "--host", "0.0.0.0", "--port", "80"]
