import requests
from bs4 import BeautifulSoup as bs

from requests import get  # to make GET request
from scrapDown import download

with requests.Session() as s:
    url = 'https://notepad-plus-plus.org/downloads/v7.9.2/'

    # Location 주소로 Get Request 호출
    html = s.get(url)
    soup = bs(html.text, 'html.parser')
    elements = soup.select('#main > p:nth-child(5) a')

    # 링크를 가져오기
    url = elements[0]['href']
    print(url)
    
    arr_url = url.split('/')
    file_name = arr_url[len(arr_url)-1]
    # download 시작
    download(url, './download/'+file_name)

