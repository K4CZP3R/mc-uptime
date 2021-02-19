FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir mcstatus pymongo

COPY database.py .
COPY log.py .
COPY main.py .
COPY uptime.py .

CMD [ "python", "-u", "./main.py" ]