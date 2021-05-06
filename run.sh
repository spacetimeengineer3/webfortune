#!/bin/bash

git clone https://github.com/spacetimeengineer3/webfortune
cd webfortune
exec bash

docker build -t wibbene/webfortune webfortune/Dockerfile

docker run -d -p  5000:5000 wibbene/webfortune


