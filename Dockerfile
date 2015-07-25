FROM ubuntu:14.04
MAINTAINER Nathan Osman <nathan@quickmediasolutions.com>

# Download and install the buildbot slave, psutil, and build-essential packages
RUN \
  apt-get update && \
  apt-get install -y buildbot-slave python-dev python-pip build-essential && \
  pip install psutil && \
  apt-get purge -y --auto-remove python-dev python-pip && \
  rm -rf /var/lib/apt/lists/*

# Copy the slave configuration and launching script
COPY buildbot.tac /var/lib/buildbot/slaves/slave/
COPY run.py /root/

# Command to setup the environment and launch the builder
CMD /root/run.py
