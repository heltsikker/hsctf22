FROM ubuntu:20.04


# update
#RUN apt update && apt upgrade

# Setup Server Environment
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev openssl socat\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# add new user if it is needed
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

# Change work directory
WORKDIR /home/ctf

# Setup the vulnerability environment
COPY source/main.py .
COPY source/flag.txt .
COPY source/secret_key.txt .

# Make sure users can't mess up for others
RUN chown -R root .


# Change user
USER ctf

# Entry point
ENTRYPOINT socat tcp-l:7000,fork,reuseaddr EXEC:"python3 main.py",stderr
