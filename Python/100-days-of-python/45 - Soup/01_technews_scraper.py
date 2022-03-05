import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

response = requests.get(URL)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
print(soup.title, soup.title.text)

article_single = soup.find(name="a", class_="titlelink")
print(article_single, article_single.get_text())
points = soup.find_all(name="span", class_="score")

article_multi = soup.find_all(name="a", class_="titlelink")

article_texts = []
article_links = []
article_points = []

for article in article_multi:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)

for art_point in points:
    point = int(art_point.getText().split(" ")[0])
    article_points.append(point)

print(article_texts)
print(article_links)
print(article_points)

largest_point_articles = max(article_points)
index = article_points.index(largest_point_articles)
print(article_texts[index], largest_point_articles)


elem = soup.find(name="h1", id="name")
elem.get("neki_atribut")

# CSS Selektor
soup.select_one(selector="p a")
soup.select_one(selector="#name")
soup.select_one(selector=".heading")