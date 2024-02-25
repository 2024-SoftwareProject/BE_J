from django.http import HttpResponse
from django.shortcuts import render


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

import bunke 

def index(request):
    return HttpResponse("testtest")


from django.http import HttpResponse
from django.shortcuts import render
from clawlingApp.models import ProductTable
import bunke 

def index(request):
    return HttpResponse("testtest")

def search_view(request):
    # URL에서 쿼리 매개변수 "query" 가져오기
    query = request.GET.get('query', '')

    # 검색 실행
    bunke.bunke_search(query)
    
    # 검색 결과를 데이터베이스에서 가져오기
    outputDB = bunke.get_products_by_category(query)
    
    # 결과를 렌더링하여 반환
    return render(request, 'search_results.html', {'outputDB': outputDB})
