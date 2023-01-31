FROM python:3.9:latest
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY . .
EXPOSE 8000
WORKDIR /client
EXPOSE 8033