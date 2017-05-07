FROM ubuntu

MAINTAINER Dane King <kingd9@gmail.com>


RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get -y install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev && \
  apt-get -y install python3 python3-dev && \
  rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install scrapy
