# Use ubuntu 20.04
FROM ubuntu:20.04

# Open port 5000
EXPOSE 5000

# update
RUN apt-get update

# install socat
RUN apt-get install socat wget -y
RUN apt-get install cron -y

# Set WorkDir
RUN mkdir /app
WORKDIR /app

# Copy binary to workdir
COPY flag.txt /flag.txt
COPY logger /app/logger
COPY lg /app/lg

# Setting cron
COPY cron /etc/cron.d/cron
COPY cron.sh /etc/cron.sh
RUN chmod 0644 /etc/cron.d/cron
RUN chmod 0744 /etc/cron.sh

RUN chown root:root logger /flag.txt
RUN chmod 755 logger /flag.txt
RUN chmod 777 /app/lg

# Securing Environment
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /bin/dash /bin/sh /bin/cat /usr/bin/id /bin/ls

# Run Program
CMD cron && socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./logger,su=nobody
