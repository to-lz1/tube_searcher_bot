#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tube_searcher_bot.tube_crawler import TubeCrawler
from tube_searcher_bot.tweeter import Tweeter
from tube_searcher_bot import config

def lambda_handler(event, context):
    result = process()
    return { 'tweetedURL': result }

def process():
    t = TubeCrawler()
    movies = []
    for keyword in config.KEYWORDS:
        movies += t.movies_from_query(keyword)
    for channel in config.CHANNELS:
        movies += t.movies_from_channel(channel)
    tw = Tweeter()
    chosen = t.choose(movies)
    
    for reply_to in config.REPLY_TO:
        tw.reply(reply_to, chosen)
    return chosen
