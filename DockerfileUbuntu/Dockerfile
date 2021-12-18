FROM ubuntu:20.04

# Set the locale
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8

#Install supplementary stuff
RUN apt-get install -y vim

#Set a user
RUN apt-get install -y sudo
RUN useradd -ms /bin/bash buddy && echo "buddy:buddy" | chpasswd && adduser buddy sudo
USER buddy
WORKDIR /home/buddy

#Set bash vi mode
RUN echo "#Vi mode" >> /home/buddy/.bashrc
RUN echo "set -o vi" >> /home/buddy/.bashrc
