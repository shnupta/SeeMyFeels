FROM mtgupf/essentia-tensorflow:latest

RUN apt-get update
RUN apt-get install -y libcairo2-dev libjpeg-dev libgif-dev
RUN pip3 install pycairo

RUN mkdir /smf

WORKDIR /smf

COPY . .

CMD ["sh", "run.sh"]
