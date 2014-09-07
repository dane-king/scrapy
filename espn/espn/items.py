# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EspnItem(scrapy.Item):
    # define the fields for your item here like:
    gameId=scrapy.Field()
    qtr = scrapy.Field()
    downDist = scrapy.Field()
    play = scrapy.Field()
    score1 = scrapy.Field()
    score2 = scrapy.Field()
