FROM python:3.6.9

RUN mkdir /var/www
WORKDIR /var/www

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
