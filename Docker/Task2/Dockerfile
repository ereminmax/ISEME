FROM ubuntu:16.04
MAINTAINER Max Eremin "eremin.max@gmail.com"
RUN apt-get update && apt-get install -y python python-dev python-distribute python-pip
COPY hello.py /tmp
CMD ["python", "tmp/hello.py"]
