# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianmaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    xianka = scrapy.Field()
    CPU = scrapy.Field()
    PMsize = scrapy.Field()
    url = scrapy.Field()
    comment = scrapy.Field()
    xiaoliang  = scrapy.Field()
    pingjia = scrapy.Field()

