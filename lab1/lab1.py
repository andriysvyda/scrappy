from requests import get
from bs4 import BeautifulSoup


BASE_URL = "https://allo.ua"
URL = f"{BASE_URL}/ua/products/notebooks/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
LAST_PAGE = 25

FILE_NAME = "laptops.txt"
with open(FILE_NAME, "w", encoding="utf-8") as file:
    for p in range(1, LAST_PAGE):
        page = get(URL, headers=HEADERS, params={"p": p})
        soup = BeautifulSoup(page.content,  "html.parser")

        items = soup.find(
            name="div", class_="products-layout__container products-layout--grid").find_all(class_="product-card")
        for item in items:
            title = item.find(
                name="a", class_="product-card__title").find(string=True, recursive=False).strip()
            price = item.find(class_="sum").find(
                string=True, recursive=False)

            print(f"Назва: {title}")
            print(f"Ціна: {price}")
            file.write(f"Назва: {title}\n")
            file.write(f"Ціна: {price}\n")