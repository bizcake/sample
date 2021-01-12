# from __future__ import print_function
import json, urllib.request
import apiData

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
from pprint import pprint


def request_fss(count=0):
    api_url = apiData.api_list['companySearch']
    fin_grp_no = '02000'
    page_no = 1

    url = f'{api_url}?auth={apiData.FINLIFE_AUTHKEY_INDI}&topFinGrpNo={fin_grp_no}&pageNo={page_no}'

    # data = urllib.request.urlopen(url).read()
    # output = json.loads(data)
    # result_code = output['result']['err_cd']
    result_code = '000'

    if result_code == '000':
        # total_count = output['result']['total_count']
        total_count = 1

        if count == 10:
            total_count = 0

        if total_count == 0:
            print('break')
        else:
            print(count)
            # function call()
            request_fss(count+1)
            pass
    else:
        print('error')
        # print(output['result']['err_msg'])

def request_opendata():
    from urllib.request import urlopen

    url = apiData.api_list['CorpBasicInfo']

    decode_key = unquote(apiData.OPEN_API_KEY)
    queryParams = '?' + urlencode({
        quote_plus('pageNo'): '100',
        quote_plus('numOfRows'): '10',
        quote_plus('resultType'): 'json',
        quote_plus('corpNm'): '메리츠자산운용',
        quote_plus('ServiceKey'): decode_key})

    print(url + queryParams)

    response = urllib.request.urlopen(url + queryParams)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        dict_ = json.loads(response_body.decode('utf-8'))
        pprint(dict_)
    else:
        print("Error Code:" + rescode)

# def urlib():
WIKI_URL = 'http://www.whatismybrowser.com'
# import urllib.request
# with urllib.request.urlopen(WIKI_URL) as response:
#     html = response.read().decode('utf-8')
#     with open('./requet.html','w', encoding='utf-8') as f:
#         f.write(html)

import requests
from bs4 import BeautifulSoup
with requests.Session() as session:
    headers = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    html2 = session.get(WIKI_URL, headers=headers).content
    with open('./requet3.html','w', encoding='utf-8') as f:
        f.write(html2.decode('utf-8'))

    # bsObj = BeautifulSoup(html, "html.parser")
    # print(type(bsObj))



# 금융감독원 API Call
# request_fss()

# 오픈API 데이터
# request_opendata()

# print(output)

import openapidata as data
json = data.json2
resultCode = json['response']['header']['resultCode']
resultMsg = json['response']['header']['resultMsg']
body = json['response']['body']
numOfRows = json['response']['body']['numOfRows']
pageNo = json['response']['body']['pageNo']
totalCount = json['response']['body']['totalCount']
item = json['response']['body']['items']["item"]
# print('item', len(item))
# print(0 < 10)
# # 10
# # 157
# print(resultCode)
# print(resultMsg)
#
# print(totalCount)
# print(pageNo)
# print(numOfRows)

page_no = 1
page_count = 10
page_sum = 0
total_count = 157

# page_sum

# for i in range(page_no, int(total_count / page_count)+1):
#     print(i)

#['items']
# 'numOfRows': 10,
# 'pageNo': 1,
# 'totalCount': 157},
# 'header': {'resultCode': '00', 'resultMsg': 'NORMAL SERVICE.'}}}

#['item']
# print(response)
# import json
# with open('openapidata.py', 'r', encoding='utf-8') as f:
#     # print( f.read() )
#     s = json.loads(f.read())
#     print(s)


