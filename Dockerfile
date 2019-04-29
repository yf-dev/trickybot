FROM python:3.7-stretch

RUN pip3 install --no-cache-dir pipenv

RUN mkdir -p /trickybot
COPY ./Pipfile /trickybot/Pipfile
WORKDIR /trickybot
RUN pipenv lock --pre
RUN pipenv install

VOLUME /trickybot
ENTRYPOINT ["pipenv", "run", "app"]
