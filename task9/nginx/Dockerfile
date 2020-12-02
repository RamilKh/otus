FROM nginx:stable-alpine

LABEL multi.name='rmpp-client-server' multi.vendor='GRFC'

# Create user www-data for run project
RUN set -x ; \
	addgroup -g 82 -S www-data ; \
	adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

# Work folder - APP FILES are mounted to here
WORKDIR /var/www/app

# Copy nginx config
COPY nginx/nginx.conf /etc/nginx/nginx.conf

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Listen port
EXPOSE 80

# Access for run
RUN chown www-data -R . && chgrp -R www-data .