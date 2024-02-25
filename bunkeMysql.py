from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# DB 연동
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

cursor = conn.cursor()

# Selenium 구동
browser = webdriver.Chrome()
browser.implicitly_wait(time_to_wait=10)
browser.get('https://m.bunjang.co.kr/')

# 검색 입력
itemname = input("검색어 입력 : ")
itemname = itemname.replace(' ', '')

Pd_Market = "번개장터"
Pd_Category = itemname

# 페이지 순환을 위한 준비 및 Get요청 쿼리
page = 0

# 페이지 순환
while True:
    page += 1
    if page == 10:
        break

    url = f"https://m.bunjang.co.kr/search/products?order=score&page={page}&q={itemname}"
    browser.get(url)
    print("*************", page, "번 Page**********************")
    
    # 대기
    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "app")))
    
    # HTML 파싱
    html = browser.page_source
    html_parser = BeautifulSoup(html, features="html.parser")

    # 상품 이미지 태그 찾기
    list = html_parser.find_all(attrs={'alt':'상품 이미지'})

    for item in list:
        parent_div = item.parent.parent  # 이미지 태그의 부모 div 태그
        name = parent_div.find('div', class_='sc-iBEsjs fqRSdX')  # 이름을 포함한 div 태그 선택 sc-hzNEM jbRqjn
        

        if(parent_div.find('div', class_='sc-etwtAo jCXDZp') or parent_div.find('div', class_='sc-clNaTc cwJWFs') or parent_div.find('div', class_='sc-hzNEM jbRqjn')):
            continue

        if name:  # name이 None이 아니라면
            print("이름 : ", name.get_text())

        Pd_Name = name.get_text()

        temp_price = parent_div.find('div', class_='sc-hzNEM bmEaky')  # 이름을 포함한 div 태그 선택하고 즉시 텍스트 추출
        temp_price = temp_price.get_text()
        temp_price = temp_price.replace(',', '')  # 쉼표 삭제

        Pd_Price = temp_price
        try:
            price = int(temp_price)  # 정수로 변환
            print("가격 : ", price)
        except ValueError:
            print("가격 형식이 올바르지 않습니다.")

        
        # 이미지 URL 출력
        if item.has_attr('src'):
            print("이미지 : {}".format(item['src']))
        else:
            print("이미지 속성을 찾을 수 없습니다.")

        Pd_IMG = item['src']
        
        # 링크 출력
        print("링크 : ", "https://m.bunjang.co.kr{}".format(parent_div.attrs['href']))

        Pd_URL = parent_div.attrs['href']
        print()

        cursor.execute("INSERT INTO ProductTable (Pd_Market, Pd_Category, Pd_name, Pd_Price, Pd_IMG, Pd_URL ) VALUES (%s, %s, %s, %s, %s, %s)", (Pd_Market, Pd_Category, Pd_Name, Pd_Price, Pd_IMG , Pd_URL))

    
    

browser.quit()
