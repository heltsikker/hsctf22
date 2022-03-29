FROM ubuntu:20.04

# Meta Information
MAINTAINER Johan Schultz Åsbakk "johan_aasbakk@msn.com"

# update
RUN apt update

# Setup Server Environment
RUN apt install -y \
    socat

# add new user if it is needed
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

# Change work directory
WORKDIR /home/ctf

# Setup the vulnerability environment
COPY source/format101 .

# Make sure users can't mess up for others
RUN chown -R root .

# Change user
USER ctf

# Entry point
ENTRYPOINT socat tcp-l:9001,fork,reuseaddr EXEC:"./format101",stderr
