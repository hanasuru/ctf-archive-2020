FROM python:latest

EXPOSE 5000

ENV SECRET_KEY 66abaada564c0210bb3d8b6aa077f4d0
ENV FLASK_APP wsgi.py
ENV FLASK_DEBUG 0

RUN mkdir -p /app/old_skool
RUN apt-get update -y
COPY old_skool/db/ /app/old_skool/db
COPY old_skool/config.py /app/old_skool/config.py
COPY old_skool/wsgi.py /app/old_skool/wsgi.py
COPY old_skool/requirements.txt /app/old_skool/requirements.txt


RUN pip install -r /app/old_skool/requirements.txt
WORKDIR /app/old_skool


RUN apt-get install -yq --no-install-recommends libgbm1 libdrm2 libxcb-dri3-0 libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 libnss3 
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs
RUN npm i puppeteer --save

COPY old_skool/application/ /app/old_skool/application
WORKDIR /app/old_skool/
COPY old_skool/visit.js /app/old_skool/visit.js

CMD flask run --host 0.0.0.0
