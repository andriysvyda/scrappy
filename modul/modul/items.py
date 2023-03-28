import scrapy


class ModulItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    file_urls = scrapy.Field()