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
COPY source/callmemaybe .
COPY source/flag.txt .

# Make sure users can't mess up for others
RUN chown -R root .

# Set up 32-bit environment
RUN set -eux
RUN dpkg --add-architecture i386
RUN apt update
RUN apt install -y libc6:i386 gcc-multilib

# Change user
USER ctf

# Entry point
ENTRYPOINT socat tcp-l:9010,fork,reuseaddr EXEC:"./callmemaybe",stderr
