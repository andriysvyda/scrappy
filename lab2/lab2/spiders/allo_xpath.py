import scrapy
from lab2.items import AlloItem


class AlloXpathSpider(scrapy.Spider):
    name = "allo_xpath"
    allowed_domains = ["allo.ua"]
    start_urls = [
        f"https://allo.ua/ua/products/notebooks/p-{page}/" for page in range(1, 5)]

    def parse(self, response):
        items = response.xpath('//div[contains(@class, "products-layout__container")]'
            ).xpath('.//*[contains(@class,"product-card")]')

        for item in items:
            name = item.xpath('.//a[contains(@class,"product-card__title")]/text()').get()
            url = item.xpath('.//a[contains(@class,"product-card__title")]/@href').get()
            price = item.xpath('.//*[@class="sum"]/text()').get()
            image_url = item.xpath('.//img/@src').get()
            yield AlloItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://allo.ua{image_url}"]
            )