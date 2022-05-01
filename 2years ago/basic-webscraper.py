# -*- coding = utf-8 -*-
# @Time : 2022/4/30 19:56
# @Author : yaowei
# @File : basic-webscraper.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import csv

book_list = []

for page in range(1,51):
    print(page)
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    article = soup.find_all('article', class_='product_pod')



    for book in article:
        title = book.find_all('a')[1]['title']
        price = book.find('p', class_='price_color').text[2:]
        instock = book.find('p', class_='instock availability').text.strip()
        books = {
            'title': title,
            'price': price,
            'instock': instock
        }
        book_list.append(books)
print(len(book_list))
# print(book_list)

with open('book_list.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = book_list[0].keys()
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(book_list)