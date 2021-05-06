#!/bin/bash

git clone https://github.com/spacetimeengineer3/webfortune

docker build -t wibbene/webfortune

docker run -p -d 5000:5000 wibbene/webfortune


