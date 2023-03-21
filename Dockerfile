FROM python:3.9.16-slim-bullseye

# set current working directory
WORKDIR /home/project

# install standard linux packages
RUN apt-get update \
    && apt-get upgrade \
    && apt-get install -y \
        git \
        make \
        nano \
        vim \
    && apt-get clean

# install python packages
COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip \
    && /usr/local/bin/python -m pip install ipython jupyterlab \
    && /usr/local/bin/python -m pip install -r requirements.txt
RUN rm requirements.txt

# set python environment variable(s)
ENV PYTHONPATH .:/home/project

# configure bash
COPY config/dockerfile/root/.bashrc /root/.bashrc

# enable jupyter access in browser
ENTRYPOINT [ \
      "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "-y", "--allow-root", \
      "--no-browser", "--NotebookApp.password=''", "--NotebookApp.token=''" \
]
