import scrapy
from bs4 import BeautifulSoup
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from lab5.items import GameItem
import time

class GamesSpider(scrapy.Spider):
    name = "games"
    allowed_domains = ["store.epicgames.com"]
    start_urls = ["https://store.epicgames.com/ru/browse?sortBy=releaseDate&sortDir=DESC&category=Game&count=40"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        gameList = soup.find(id="css-cnqlhg")
        for game in gameList:
            if game:
                name = game.find(class_="css-rgqwpc").find(string=True, recursive=False)
                url = game.find(class_="css-g3jcms").get("href")
                price = game.find(class_="css-119zqif").find(string=True, recursive=False)
                yield AnimeItem(
                    name=name,
                    url=url,
                    price=price
                )