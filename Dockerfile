from ubuntu:latest

RUN sudo apt install python3-pip

RUN sudo apt update
RUN pip install --upgrade tensorflow

