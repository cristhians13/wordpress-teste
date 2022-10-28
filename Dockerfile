FROM wordpress:apache

RUN rm -r /var/www/html/*

COPY . /var/www/html/

RUN chown -R www-data:www-data /var/www/html/

ENTRYPOINT ["apache2-foreground"]