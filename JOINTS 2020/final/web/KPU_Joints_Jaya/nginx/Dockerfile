FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /www/data/
COPY static/ /www/data/ 
