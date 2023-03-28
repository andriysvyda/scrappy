import scrapy
from bs4 import BeautifulSoup
from modul.items import ModulItem

class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/fashion/sumki/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="list-body").find_all(class_="list-item list-item--row")
        for item in items:
            name = item.find(name="a", class_="list-item__title-container m_b-5").find(string=True, recursive=False).strip()
            url = item.find(name="a", class_="list-item__title-container m_b-5").get("href")
            price = item.find(class_="promo-list-item__value-offers").find(string=True, recursive=False)
            image_url = item.find(name="img").get("src")
            yield ModulItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://hotline.ua/{image_url}"]
            )