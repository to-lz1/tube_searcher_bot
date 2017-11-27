#!/usr/bin/env bash

rm lambda.zip

cd src
pip3 install -r requirements.txt -t ./lib
zip ../lambda.zip *.py
cd lib
zip -r ../../lambda.zip *
