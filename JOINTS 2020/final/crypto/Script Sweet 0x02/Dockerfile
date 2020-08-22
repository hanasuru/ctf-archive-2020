FROM python:latest

RUN groupadd -g 666 nobodi
RUN useradd -r -u 666 -g nobodi -m nobodi

RUN pip install pycryptodome
RUN apt-get update -y
RUN apt-get install socat -y
COPY main.py secret.py flag.txt /home/nobodi/
WORKDIR /home/nobodi
RUN chmod +x main.py
USER nobodi

CMD socat TCP-LISTEN:9997,reuseaddr,fork EXEC:./main.py
