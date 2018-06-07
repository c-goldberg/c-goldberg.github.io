from bs4 import BeautifulSoup
from urllib import request
url = "https://github.com/humanitiesprogramming/scraping-corpus"
html = request.urlopen(url).read()
print(html[0:2000])
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('a')[0:10])
for item in soup.find_all('a')[0:10]:
    print('=======')
    print(item.text.replace('\n', ''))

for link in soup.select("td.content a"):
    print(link.text)

links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href']
    urls.append(url)
print(urls)

links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)
print(urls)

corpus_texts = []
for url in urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)

print(corpus_texts)
