#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random
import re
from crawler import Crawler

class TubeCrawler(Crawler):

    URLBase = "https://www.youtube.com"

    def hrefs_from_channel(self, channel_id):
        """
        :param str channel_id: YouTube Channel Id to crawl
        :rtype: set of str
        :return: all href parameters
        """
        return super().hrefs_from(self.URLBase + "/channel/" + channel_id)


    def hrefs_from_query(self, key_phrase):
        """
        :param str key_phrase: key phrase to search YouTube
        :rtype: set of str
        :return: all href parameters
        """
        return super().hrefs_from(self.URLBase + \
            "/results?search_query=" + key_phrase.replace(" ", "+"))


    def hrefs_from_list(self, list_id):
        """
        :param str list_id: YouTube list Id to crawl
        :rtype: set of str
        :return: all href parameters
        """
        return super().hrefs_from(self.URLBase + "/playlist?list=" + list_id)


    def movies_from_channel(self, channel_id, max_count = 10):
        """
        :param str channel_id: YouTube Channel Id to crawl
        :param int max_count: max count to return
        :rtype: list of str
        :return: list of movie ids contained in Channel top page
        """
        return self.__select_movies(self.hrefs_from_channel(channel_id), max_count)


    def movies_from_query(self, key_phrase, max_count = 10):
        """
        :param str key_phrase: key phrase to search YouTube
        :param int max_count: max count to return
        :rtype: list of str
        :return: list of movie ids contained in result first page
        """
        return self.__select_movies(self.hrefs_from_query(key_phrase), max_count)


    def movies_from_list(self, list_id, max_count = 10):
        """
        :param str channel_id: YouTube list Id to crawl
        :param int max_count: max count to return
        :rtype: list of str
        :return: list of movie ids contained in the list
        """
        return self.__select_movies(self.hrefs_from_list(list_id), max_count)


    def choose(self, movie_ids, prefix = "https://youtu.be/"):
        """
        :param list of str movie_ids: list of movie id
        :param str prefix: prefix of returned string, generally to make some valid URL
        :rtype: str
        :return: a movie chosen at random
        """
        return prefix + random.choice(movie_ids)


    def __select_movies(self, hrefs, max_count):
        """
        :param set of str hrefs: set of raw href parameters
        :param int max_count: max count to return
        :rtype: list of str
        :return: list of str that can be recognized as a YouTube movie id
        """
        filtered = [ re.sub( "^.*/watch\?v=", "", re.sub( "&(list|index)=.*$", "", href )) \
            for href in hrefs if "/watch?v=" in href ]
        return filtered[:min(max_count, len(filtered))]
