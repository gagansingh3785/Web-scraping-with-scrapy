# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtyvisItem(scrapy.Item):
	Name = scrapy.Field()
	Description = scrapy.Field()
	Cost = scrapy.Field()
	Images = scrapy.Field()
   
