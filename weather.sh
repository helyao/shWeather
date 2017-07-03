#!/bin/bash

source /home/helyao/anaconda2/envs/py27/bin/activate py27

python --version

cd /home/helyao/github/shWeather/SHWeather

scrapy crawl weather

echo 'Finish Weather Spider\n'