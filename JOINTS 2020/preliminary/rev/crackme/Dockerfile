FROM ubuntu:18.04

RUN apt-get update

# utf-8
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# app
RUN apt-get install -y socat

RUN groupadd -g 666 crackme
RUN useradd -r -u 666 -g crackme -m crackme

RUN mkdir /home/crackme/services
COPY ./crackme.c /home/crackme/services/
COPY ./crackme /home/crackme/services/
COPY ./flag.txt /home/crackme/services
RUN chmod +x /home/crackme/services/crackme
RUN chmod +r /home/crackme/services/flag.txt 
WORKDIR /home/crackme/services/

USER crackme

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./crackme
