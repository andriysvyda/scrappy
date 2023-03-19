import scrapy
from bs4 import BeautifulSoup
from lab2.items import AlloItem

class AlloSpider(scrapy.Spider):
    name = "allo"
    allowed_domains = ["allo.ua"]
    start_urls = [
        f"https://allo.ua/ua/products/notebooks/p-{page}/" for page in range(1, 5)]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="products-layout__container products-layout--grid").find_all(class_="product-card")
        for item in items:
            name = item.find(name="a", class_="product-card__title").find(string=True, recursive=False).strip()
            url = item.find(name="a", class_="product-card__title").get("href")
            price = item.find(class_="sum").find(string=True, recursive=False)
            image_url = item.find(name="img").get("src")
            yield AlloItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://allo.ua{image_url}"]
            )