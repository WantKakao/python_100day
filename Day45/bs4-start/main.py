from bs4 import BeautifulSoup
import lxml, requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
# print(response.text)

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.select('.titleline > a')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all('span', class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_num = max(article_upvotes)
largest_idx = article_upvotes.index(largest_num)
print(largest_idx)
print(article_texts[largest_idx])
print(article_links[largest_idx])









# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())

# all_anchor_tag = soup.find_all("a")
#
# for tag in all_anchor_tag:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(id='name')
# print(heading)

# section_heading = soup.find_all(class_='heading')
# print(section_heading)

# company_url = soup.select_one("p a")
# print(company_url)
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)