# -*- coding = utf-8 -*-
# @Time : 2022/4/14 19:48
# @Author : yaowei
# @File : step.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
wine_list = []

# Step 1 - Request

def step_one(x):
    url = f'http://wanderlustwine.co.uk/buy-wine-online/page/{x}/'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, features='lxml')
    return soup

# step 2 - Parse
def parse(soup):
    products = soup.find_all('li', class_='product')
    for item in products:
        try:
            product = {
                "name": item.find('h2').text.strip(),
                "price": item.find('span', class_='price').text
            }
            wine_list.append(product)
        except:
            pass

# Step 3 - Output
def output():
    df = pd.DataFrame(wine_list)
    df.to_csv('00winelist.csv', index=False)

def main():
    for x in range(4,11):
        print(f'Getting page{x}')
        html = step_one(x)
        print('Parsing...')
        parse(html)

    output()
    print('Save to CSV.')
