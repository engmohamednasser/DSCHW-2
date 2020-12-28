#!/bin/sh
sudo docker build -t pythimage .
sudo docker volume create volume

sudo docker run pythimage


