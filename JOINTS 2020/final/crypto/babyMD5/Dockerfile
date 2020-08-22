FROM python:2.7

EXPOSE 5000
RUN groupadd -g 666 nobodi
RUN useradd -r -u 666 -g nobodi -m nobodi

RUN apt-get update -y
RUN apt-get install socat -y
COPY babyMD5.py flag.txt /home/nobodi/

WORKDIR /home/nobodi
RUN chmod 755 babyMD5.py

#specific user
USER nobodi

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./babyMD5.py
