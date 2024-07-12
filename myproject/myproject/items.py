# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MyItem(scrapy.Item):
    museum = scrapy.Field()
    city = scrapy.Field()
    emails = scrapy.Field()
    phones = scrapy.Field()
    url = scrapy.Field()