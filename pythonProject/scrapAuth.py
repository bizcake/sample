import requests
from bs4 import BeautifulSoup as bs


LOGIN_URL = 'http://prv.ph-core.com//lib/submit.php?sbmpage=/page/member/signin.sbm.php'
LOGIN_INFO = {
    'id': 'admin',
    'pass': 'test1234'
}

with requests.Session() as s:
    res = s.post(LOGIN_URL, data=LOGIN_INFO, verify=False, allow_redirects=False)

    # 쿠키와 헤더에 포함된 302 Location 값을 가져온다.
    # 이때, 헤더에 설정된 쿠키와 함께 Location으로 Get Request 를 보내면 된다.
    print( res.headers )
    redirect_cookie = res.headers['Set-Cookie']
    # redirect_url = res.headers['Location'] == None ? res.headers['Location'] : ''
    redirect_url = 'http://prv.ph-core.com'
    headers = {"Cookie": redirect_cookie}

    # Location 주소로 Get Request 호출
    html = s.get(redirect_url, headers=headers)
    # print(html.content)

    soup = bs(html.text, 'html.parser')
    print(soup)

    # elements = soup.select('dt > a')
    # elements.get('href')  # 링크를 가져오고 싶다면!
# https://notepad-plus-plus.org/downloads/v7.9.2/