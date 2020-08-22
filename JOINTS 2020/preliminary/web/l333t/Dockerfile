FROM python:latest

EXPOSE 5000

ENV SECRET_KEY d55caf5b89e171db3ee808ab42edcd0b
ENV FLASK_APP wsgi.py
ENV FLASK_DEBUG 0

RUN mkdir -p /app/leet_code
RUN apt-get update -y
COPY leet_code/db/ /app/leet_code/db
COPY leet_code/config.py /app/leet_code/config.py
COPY leet_code/wsgi.py /app/leet_code/wsgi.py
COPY leet_code/requirements.txt /app/leet_code/requirements.txt


RUN pip install -r /app/leet_code/requirements.txt
WORKDIR /app/leet_code


RUN apt-get install -yq --no-install-recommends libgbm1 libdrm2 libxcb-dri3-0 libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 libnss3 
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs
RUN npm i puppeteer --save

COPY leet_code/application/ /app/leet_code/application
WORKDIR /app/leet_code/
COPY leet_code/visit.js /app/leet_code/visit.js
RUN pip install requests
CMD flask run --host 0.0.0.0