import requests
from bs4 import BeautifulSoup as bs

from requests import get  # to make GET request

def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url)               # get request
        file.write(response.content)      # write to file

if __name__ == '__main__':
    url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9.2/npp.7.9.2.portable.zip"
    arr_url = url.split('/')
    file_name = arr_url[len(arr_url)-1]
    download(url, './download/'+file_name)
