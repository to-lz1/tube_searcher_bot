#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
from tube_searcher_bot import config

def getOAuth():
  return OAuth1Session(
  config.CONSUMER_KEY,
  config.CONSUMER_SECRET,
  config.ACCESS_TOKEN,
  config.ACCESS_TOKEN_SECRET)
