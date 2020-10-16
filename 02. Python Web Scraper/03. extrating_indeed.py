import requests as req
from bs4 import BeautifulSoup as bs

indeed_result = req.get("https://kr.indeed.com/jobs?q=python&l=seoul")

indeed_soup = bs(indeed_result.text, "html.parser")

# <div class="pagination" onmousedown="pclk(event);">
pagination = indeed_soup.find("div", {"class": "pagination"})

# #resultsCol > nav > div > ul > li:nth-child(4) > a
# <a href="/jobs?q=python&amp;l=seoul&amp;start=30" aria-label="4"
# pages is a list
links = pagination.find_all('a')

pages = []
for link in links[:-1]:
    # pages.append(link.find("span").string) // is same as the one below
    pages.append(int(link.string))
# <span class="pn">2</span>
max_page = pages[-1]

# print(pages)
# print(max_page)
# print(range(max_page))

for n in range(max_page):
    print(f"start={n*800}")