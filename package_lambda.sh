#!/usr/bin/env bash

rm lambda.zip

# Download all dependencies.
pipenv lock -r > requirements.txt
pipenv run pip install -t ./vendor -r requirements.txt

zip -r9 lambda.zip setup.py tube_searcher_bot/

pushd vendor
zip -r9 ../lambda.zip *
