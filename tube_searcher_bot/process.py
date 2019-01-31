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
    movies = t.movies_from_query("Hybrid Rudiments")
    movies += t.movies_from_query("Steve Gadd Lick")
    movies += t.movies_from_list("PLleS-Mfyj_fcVg4KxLTARvklDuObTd9zc", 15)
    tw = Tweeter()
    chosen = t.choose(movies)
    tw.reply(config.REPLY_TO, chosen)
    return chosen
