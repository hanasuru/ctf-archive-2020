FROM python:2.7

EXPOSE 5000
RUN groupadd -g 666 nobodi
RUN useradd -r -u 666 -g nobodi -m nobodi

RUN apt-get update -y
RUN apt-get install python-pip -y
RUN apt-get install socat -y
COPY babyRSA.py secret.py /home/nobodi/

WORKDIR /home/nobodi
RUN chmod 755 babyRSA.py

#specific user
USER nobodi
RUN pip install pycrypto --user
RUN pip install gmpy --user

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./babyRSA.py
