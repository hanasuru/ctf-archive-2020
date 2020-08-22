FROM python:latest

EXPOSE 5000
RUN groupadd -g 666 nobodi
RUN useradd -r -u 666 -g nobodi -m nobodi

RUN apt-get update -y
RUN apt-get install socat -y
COPY main.py /home/nobodi
WORKDIR /home/nobodi
RUN chmod 755 main.py
USER nobodi

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./main.py