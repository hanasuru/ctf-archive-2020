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

RUN groupadd -g 666 goRev
RUN useradd -r -u 666 -g goRev -m goRev

RUN mkdir /home/goRev/services
COPY ./goRev.go /home/goRev/services/
COPY ./goRev /home/goRev/services/
COPY ./flag.txt /home/goRev/services
RUN chmod +x /home/goRev/services/goRev
RUN chmod +r /home/goRev/services/flag.txt 
WORKDIR /home/goRev/services/

USER goRev

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./goRev
