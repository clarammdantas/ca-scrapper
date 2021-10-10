# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ExpressEntryItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DrawItem(Item):
    round_id = Field()
    date = Field()
    immigration_program = Field()
    invitations_issued = Field()
    crs_score = Field()
