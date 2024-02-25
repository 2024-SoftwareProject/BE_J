from bs4 import BeautifulSoup
import requests

# 웹 페이지 URL 설정
url = 'https://m.bunjang.co.kr/search/products?order=score&page=1&q=맥북에어'

print(1)

# 해당 웹 페이지에 GET 요청을 보내고 응답을 받아옴
response = requests.get(url)
print(2)
# 응답의 HTML 텍스트를 BeautifulSoup으로 파싱
# soup = BeautifulSoup(response.text, 'html.parser')

soup = BeautifulSoup(response.text, features="html.parser")

print(3)
# alt 속성 값이 '상품 이미지'로 설정된 모든 요소 찾기
list = soup.find_all(attrs={'alt': '상품 이미지'})
print(4)
# 결과 출력
for element in list:
    print(element)

    a= element.parent.parent
    print("정보 : ", a.get_text(separator=';;;'))
        # print("링크 : ", "https://m.bunjang.co.kr{}".format(aTag.attrs['href']))
        # st = item.parent.parent.get_text(separator=';;;')

print(5)
