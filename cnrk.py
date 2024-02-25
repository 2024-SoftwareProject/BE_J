# import requests
# from bs4 import BeautifulSoup

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',"accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# item = '아이폰'

# url = f'https://m.bunjang.co.kr/search/products?q={item}'
# # url = 'https://m.bunjang.co.kr/search/products?q=아이폰&ref=검색결과'

# res = requests.get(url, headers=headers)

# # print(res)
# soup = BeautifulSoup(res.text, "lxml")

# div_tag = soup.find('div', id='root') 
# div_tags = div_tag.find('div', class_='app sc-hGoxap.bInodS sc-ejGVNB.eUyMEm sc-eLdqWK.jBsZbG sc-jKmXuR.hQiBRl sc-eTpRJs.ekyrKV ')

# # 모든 div 태그를 찾아서 리스트로 반환합니다.
# div_tags = div_tags.find_all('div')

# # 찾아낸 div 태그들을 출력합니다.
# for div in div_tags:
#     print(div)

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}
item = '아이폰'

url = f'https://m.bunjang.co.kr/search/products?q={item}'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

root_div = soup.find("div", id="root")
inner_divs = root_div.find_all("class")
print(root_div)
print(inner_divs)

for div in inner_divs:
    print(div.text)


# div_elements = soup.find_all(lambda tag: tag.name.startswith('div'))
# div_elements = div_elements[:10]
# for div in div_elements:
#     print(div)


# # id가 "root"인 div 요소를 찾습니다.
# root_div = soup.find('div', id='root')

# print(soup.find('div', attrs={"class": "sc-iBEsjs.fqRSdX"}))

# test1 = root_div.find('div',class_='app')
# print(root_div)
# print(test1)

# root_div = soup.find('div', {"class":"app"})
# # test1  = root_div.find('div', {"class":"app"})

# print(root_div)
# print(test1)

