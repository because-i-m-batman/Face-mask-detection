from ubuntu:latest

RUN apt install python3-pip

RUN apt update
RUN pip install --upgrade tensorflow

