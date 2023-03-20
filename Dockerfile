FROM python:3.9.16-slim-bullseye

RUN apt update \
    && apt upgrade \
    && apt install git -y \
    && apt install make -y\
    && apt install vim -y

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip \
    && /usr/local/bin/python -m pip install -r requirements.txt
RUN rm requirements.txt

COPY config/dockerfile/root/.bashrc /root/.bashrc
