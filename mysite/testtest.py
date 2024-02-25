from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

def testkk():
    browser = webdriver.Chrome()
    browser.implicitly_wait(time_to_wait=10)
    browser.get('https://m.bunjang.co.kr/')

    browser.close()