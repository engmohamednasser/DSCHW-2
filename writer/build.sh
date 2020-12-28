#!/bin/sh
sudo docker build -t pythimage2 .
sudo docker volume create volume
sudo docker run --rm -v $(pwd)/volume:/pythimage2



