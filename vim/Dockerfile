FROM python:3
MAINTAINER vimpython "w@wktadmin.com"
RUN  apt-get update -y  && apt-get install sudo  -y
WORKDIR /root/
RUN git clone https://github.com/sazima/legolas-vim.git
WORKDIR /root/legolas-vim
RUN bash install.sh INIT 
RUN bash install-plugins.sh install

