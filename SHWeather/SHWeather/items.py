# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShweatherItem(scrapy.Item):
    time = scrapy.Field()
    wea_from = scrapy.Field()
    wea_to = scrapy.Field()
    tem_from = scrapy.Field()
    tem_to = scrapy.Field()
    win_from = scrapy.Field()
    win_to = scrapy.Field()

