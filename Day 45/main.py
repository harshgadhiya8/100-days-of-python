from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
# titles = soup.select(selector='td a')
# for title in titles:
#     print(title.get_text())
texts = []
links = []
articles = soup.select(".titleline a")
for article in articles:
    texts.append(article.getText())
for article in articles:
    links.append(article.get("href"))
article_upvotes = []
upvotes = soup.find_all(name='span',class_='score')
for upvote in upvotes:
    article_upvotes.append(int(upvote.getText().split()[0]))

# print(links)
# print(texts)
# print(article_upvotes)

index = article_upvotes.index(max(article_upvotes))
print(links[index])
print(texts[index])
print(article_upvotes[index])






# with open('website.html',encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents,'html.parser')
# print(soup.title)
# print(soup.h1.string)
# print(soup.prettify())
# anchor_text = soup.find_all(name='a')
# for text in anchor_text:
#     # print(text.getText())
#     print(text.get("href"))

# heading = soup.find(name='h1')
# print(heading.string)
# section_heading = soup.find(name='h3',class_='heading')
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a").get("href")
# print(company_url)