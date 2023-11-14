FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt start_server.sh /
RUN pip install -r /requirements.txt

RUN perl -pi -e 's/\r\n|\n|\r/\n/g' /start_server.sh

ENV APP_HOME=/var/www
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles

WORKDIR $APP_HOME

COPY . $APP_HOME

RUN chmod +x /start_server.sh
RUN chown -R www-data:www-data ${APP_HOME}

CMD ["/bin/sh", "/start_server.sh"]
