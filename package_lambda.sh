#!/usr/bin/env bash

rm lambda.zip

# Download all dependencies.
pipenv lock -r > requirements.txt
pipenv run pip download -d ./tube_searcher_bot/vendor -r requirements.txt

zip -r lambda.zip tube_searcher_bot/
zip lambda.zip setup.py
