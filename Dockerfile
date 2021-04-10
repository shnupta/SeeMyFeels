FROM mtgupf/essentia-tensorflow:latest

RUN apt-get update
RUN apt-get install -y libcairo2-dev libjpeg-dev libgif-dev pkg-config python3-dev

RUN mkdir /smf

WORKDIR /smf

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/smf

RUN pip3 install -r requirements.txt

CMD ["sh", "run.sh"]

EXPOSE 8080
