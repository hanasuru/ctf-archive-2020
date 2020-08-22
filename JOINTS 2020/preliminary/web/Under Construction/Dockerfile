FROM python:latest

EXPOSE 5000

ENV SECRET_KEY dbd74660c312262fabad1b001bde197c
ENV FLASK_APP wsgi.py
ENV FLASK_DEBUG 0

RUN mkdir -p /app/under_construction
RUN apt-get update -y
COPY under_construction/db/ /app/under_construction/db
COPY under_construction/config.py /app/under_construction/config.py
COPY under_construction/wsgi.py /app/under_construction/wsgi.py
COPY under_construction/requirements.txt /app/under_construction/requirements.txt


RUN pip install -r /app/under_construction/requirements.txt
WORKDIR /app/under_construction


RUN apt-get install -yq --no-install-recommends libgbm1 libdrm2 libxcb-dri3-0 libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 libnss3 
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs
RUN npm i puppeteer --save

COPY under_construction/application/ /app/under_construction/application
WORKDIR /app/under_construction/
COPY under_construction/visit.js /app/under_construction/visit.js

CMD flask run --host 0.0.0.0
