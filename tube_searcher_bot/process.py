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
    # todo: enable array configuration and iteration
    movies = t.movies_from_query(config.KEYWORD_1)
    movies += t.movies_from_query(config.KEYWORD_2)
    movies += t.movies_from_list(config.CHANNEL, 15)
    tw = Tweeter()
    chosen = t.choose(movies)
    tw.reply(config.REPLY_TO, chosen)
    return chosen
