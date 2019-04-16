FROM python:3.7-stretch

RUN pip3 install --no-cache-dir pipenv  -i http://mirror.kakao.com/pypi/simple --trusted-host mirror.kakao.com

RUN mkdir -p /trickybot
COPY ./Pipfile /trickybot/Pipfile
WORKDIR /trickybot
RUN pipenv install

VOLUME /trickybot
ENTRYPOINT ["pipenv", "run", "app"]
