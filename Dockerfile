FROM ubuntu:20.04

ENV LANG C.UTF-8

ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get -y upgrade

RUN apt-get install -y python3-dev python3-pip git \
    && pip3 install tensorflow \
    && git clone https://github.com/MTG/essentia.git \ 
    && cd essentia && src/3rdparty/tensorflow/setup_from_python.sh \
    && apt-get install -y build-essential libyaml-dev libfftw3-dev libavcodec-dev libavformat-dev libavutil-dev libavresample-dev python-dev libsamplerate0-dev libtag1-dev libchromaprint-dev python-six python3-dev python3-numpy-dev python3-numpy python3-yaml libeigen3-dev vim wget \
    && python3 waf configure --build-static --with-python --with-tensorflow \
    && python3 waf \
    && python3 waf install

RUN mkdir /smf

ENV PYTHONPATH /usr/local/lib/python3/dist-packages

WORKDIR /smf
