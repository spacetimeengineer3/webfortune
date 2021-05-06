#!/bin/bash

git clone https://github.com/spacetimeengineer3/webfortune
cd webfortune
docker build -t .

docker run -d -p  5000:5000 wibbene/webfortune


