#!/bin/bash
yes | apt-get update
yes | apt-get install zip unzip rsync python3-pip
yes | curl -sL https://aka.ms/InstallAzureCLIDeb | bash
yes | apt-get install curl && curl -sL https://deb.nodesource.com/setup_12.x | bash
yes | apt-get install nodejs
yes | npm install -g azure-functions-core-tools@3 --unsafe-perm true
