# -*- coding = utf-8 -*-
# @Time : 2022/4/17 19:25
# @Author : yaowei
# @File : newmethod.py
# @Software : PyChar
from requests_html import HTMLSession

urls = [
    'https://www.amazon.com/-/zh/dp/B09JQKBQSB/ref=sr_1_2?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=3M4N7IFDCJ6EN&keywords=macbook&qid=1650197317&sprefix=macbook%2Caps%2C510&sr=8-2',
    'https://www.amazon.com/-/zh/dp/B082J572X8/ref=sr_1_5?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=3M4N7IFDCJ6EN&keywords=macbook&qid=1650197317&sprefix=macbook%2Caps%2C510&sr=8-5',
    'https://www.amazon.com/-/zh/dp/B01LZORCUR/ref=sr_1_7?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=3M4N7IFDCJ6EN&keywords=macbook&qid=1650197317&sprefix=macbook%2Caps%2C510&sr=8-7'
]
def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    print(r)
    print(type(r))
    r.html.render(sleep=200)

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]', first=True).text
    }
    print(product)
    return product

macprict = []
for url in urls:
    price = getPrice(url)
    macprict.append(price)
print(macprict)