#!/bin/sh

set -e
set -u

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    git \
    curl \
    wget \
    vim \
    gnupg2 \
    python3 \
    python3-apt \
    python-apt \
    python-setuptools \
    python-pip \
    software-properties-common

# Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/debian/gpg \
	| sudo apt-key add -

add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
apt-get update


# Install the latest version of Docker CE and containerd
apt-get install -y docker-ce docker-ce-cli containerd.io

# Install docker-compose
if [ ! -f /usr/local/bin/docker-compose ]; then
	sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" \
		-o /usr/local/bin/docker-compose.tmp
	chmod +x /usr/local/bin/docker-compose.tmp
	mv /usr/local/bin/docker-compose.tmp /usr/local/bin/docker-compose
fi

# Setup permissions
if ! grep 'docker:.*vagrant' ; then
	adduser vagrant docker
fi

# Install python
apt-get install -y \
    python3-pip vim git

echo "SUCCESS."
