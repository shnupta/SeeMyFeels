FROM mtgupf/essentia-tensorflow:latest

RUN mkdir /smf

WORKDIR /smf

COPY . .

CMD ["sh", "run.sh"]
