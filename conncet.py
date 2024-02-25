#중고나라에서 상품이름과 상품 가격표시및 데베 저장 
import requests
from bs4 import BeautifulSoup
import pymysql

# MySQL 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root', 
    password='seeun0303!',  
    database='mydb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# User-Agent 지정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

# 중고나라에서 크롤링할 페이지 수
pages_to_crawl = 3

current_products = set()

for page in range(1, pages_to_crawl + 1):
    # URL 설정
    url = f"https://web.joongna.com/search/%EB%A7%A5%EB%B6%81%ED%94%84%EB%A1%9C?page={page}"

    # 해당 url의 html 가져오기
    res = requests.get(url, headers=headers)

    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(res.text, "html.parser")

    # 상품 이름과 가격 가져오기
    products = soup.find_all("h2", class_="line-clamp-2 text-sm md:text-base text-heading")
    prices = soup.find_all("div", class_="font-semibold space-s-2 mt-0.5 text-heading lg:text-lg lg:mt-1.5")
    print(prices)
    print("\n ---------- \n")
    images = soup.find_all("img", class_="bg-gray-300 object-cover h-full w-full transition duration-200 ease-in rounded-md group-hover:rounded-b-none")
    
    # 현재 페이지에서 크롤링한 상품들을 집합에 추가
    for product in products:
        current_products.add(product.text.strip())

print(prices) 

# 데이터베이스에 저장된 상품들을 가져와서 현재 판매 중인 상품들과 비교
with conn.cursor() as cursor:
    # 데이터베이스에 저장된 모든 상품 가져오기
    cursor.execute("SELECT product_name FROM products")
    stored_products = set(row['product_name'] for row in cursor.fetchall())

    # 데이터베이스에 저장된 상품과 현재 판매 중인 상품들을 비교하여 삭제할 상품들 찾기
    products_to_delete = stored_products - current_products

    # 삭제할 상품들을 데이터베이스에서 삭제
    for product_name in products_to_delete:
        cursor.execute("DELETE FROM products WHERE product_name = %s", (product_name,))
    conn.commit()

    
    # 결과 출력 및 데이터베이스에 저장
    with conn.cursor() as cursor:
        for product, price, image in zip(products, prices, images):
            product_name = product.text.strip()
            product_price = price.text.strip()
            product_image = image['src'] #이미지 태그에서 src 속성 추출 

            # 결과 출력
            print("상품명:", product_name)
            print("가격:", product_price)
            print("이미지:", product_image)
            print("-" * 20)

            # 데이터베이스에 저장
            cursor.execute("INSERT INTO products (product_name, product_price, product_image) VALUES (%s, %s, %s)", (product_name, product_price, product_image))
            conn.commit()

# 연결 종료
conn.close()