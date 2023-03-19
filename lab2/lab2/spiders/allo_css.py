import scrapy
from lab2.items import AlloItem


class AlloCssSpider(scrapy.Spider):
    name = "allo_css"
    allowed_domains = ["allo.ua"]
    start_urls = [
        f"https://allo.ua/ua/products/notebooks/p-{page}/" for page in range(1, 5)]

    def parse(self, response):
        items = response.css('div.products-layout__container').css('.product-card')

        for item in items:
            name = item.css('a.product-card__title::text').get()
            url = item.css('a.product-card__title::attr(href)').get()
            price = item.css('.sum::text').get()
            image_url = item.css('img::attr(src)').get()
            yield AlloItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://allo.ua{image_url}"]
            )