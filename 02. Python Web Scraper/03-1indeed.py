import requests as req
from bs4 import BeautifulSoup as bs

INDEED_URL = "https://kr.indeed.com/jobs?q=python&l=seoul&sort=date"

def extract_indeed_pages():
    result = req.get(INDEED_URL)

    soup = bs(result.test, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:1]:
        pages.append((int(link.string)))

    max_page = pages[-1]

    return max_page
