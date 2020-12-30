FROM python:3.8

RUN apt-get update \ 
    && apt-get install -y git ffmpeg libsm6 libxext6 \
    && export PATH=$PATH:~/.local/bin

# Jupyter Notebook
EXPOSE 8000-9999
