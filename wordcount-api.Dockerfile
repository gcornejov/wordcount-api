from ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.10 -y
RUN apt install python3-pip -y

WORKDIR /wordcount-api
COPY . /wordcount-api

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT  ["python3"]
CMD ["app.py"]
