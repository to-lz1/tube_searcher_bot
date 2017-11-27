#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import config

def getOAuth():
  return OAuth1Session(
  config.CONSUMER_KEY,
  config.CONSUMER_SECRET,
  config.ACCESS_TOKEN,
  config.ACCESS_TOKEN_SECRET)
