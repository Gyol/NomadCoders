import requests as req
from bs4 import BeautifulSoup as bs


START = 10
URL = f"https://kr.indeed.com/jobs?q=python&l=seoul&sort=date"


def extract_indeed_pages():
    result = req.get(URL)

    soup = bs(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append((int(link.string)))

    max_page = pages[-1]

    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = req.get(f"{URL}&start={page*START}")
        print(result.status_code)
