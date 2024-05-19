#Ubuntu is the base image which is used for containerization
FROM ubuntu

WORKDIR /app

COPY requirements.txt /app
COPY app /app

RUN apt-get update && \
apt-get install python3 python3-pip && \
pip install -r requirements.txt

CMD [ "python3","main.py" ]

