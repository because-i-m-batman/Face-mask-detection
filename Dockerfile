from ubuntu:latest

RUN apt-get update
RUN apt-get install python3-pip python3-dev
RUN pip3 --no-cache-dir install --upgrade pip 

RUN apt update
RUN pip3 install --upgrade tensorflow

