FROM nginx:1.21-alpine

RUN rm -rf /etc/nginx/conf.d

COPY conf.d /etc/nginx/conf.d
COPY run.sh /etc/nginx

CMD ["sh", "/etc/nginx/run.sh"]