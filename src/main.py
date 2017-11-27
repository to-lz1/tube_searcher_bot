#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tube_crawler import TubeCrawler
from tweeter import Tweeter
import config

def main():
    t = TubeCrawler()
    movies = t.movies_from_query("Hybrid Rudiments")
    movies += t.movies_from_query("Steve Gadd Lick")
    movies += t.movies_from_list("PLleS-Mfyj_fcVg4KxLTARvklDuObTd9zc", 15)
    tw = Tweeter()
    chosen = t.choose(movies)
    tw.reply(config.REPLY_TO, chosen)
    return chosen

def lambda_handler(event, context):
    result = main()
    return { 'tweetedURL': result }

if __name__ == '__main__':
    main()
