#중고나라에서 상품이름과 상품 가격표시및 데베 저장 
import requests
from bs4 import BeautifulSoup
import pymysql

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

# 중고나라에서 크롤링할 페이지 수
pages_to_crawl = 1
search = '맥북'

current_products = set()

for page in range(1, pages_to_crawl + 1):
    # URL 설정
    url = f"https://www.daangn.com//search/{search}?page={page}"
    print(url)

    # 해당 url의 html 가져오기
    res = requests.get(url, headers=headers)

    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(res.text, "html.parser")

    # 상품 이름과 가격 가져오기
    products = soup.find_all("span", class_="article-title")
    prices = soup.find_all("p", class_="article-price")
    alpha = soup.find_all("article", {"class": "flea-market-article flat-card", "data-next-page": "3"})
    # images = soup.find_all("img", class_="bg-gray-300 obj
    # ect-cover h-full w-full transition duration-200 ease-in rounded-md group-hover:rounded-b-none")
    
 
    print("상품명:", products)
    print("가격:", prices)

    print()

    print(alpha)