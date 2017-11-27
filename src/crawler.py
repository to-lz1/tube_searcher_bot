#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

class Crawler:
    def hrefs_from(self, URL):
        a_tags = self.soup_from(URL).find_all("a", href=True)
        return set(map(lambda a:a["href"], a_tags))

    def soup_from(self, URL):
        res_text = requests.get(URL).text
        try:
            return BeautifulSoup(res_text, "lxml")
        except:
            return BeautifulSoup(res_text, "html5lib")
