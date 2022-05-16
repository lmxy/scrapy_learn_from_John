# -*- coding = utf-8 -*-
# @Time : 2022/5/1 15:36
# @Author : yaowei
# @File : test_f.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.dxd365.com/friends-720p-bluray-x264/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

res = requests.get(url, headers=headers)
# print(res.text)
soup = BeautifulSoup(res.text, "lxml")
links = soup.select('div.article-body > p > a')
print(links)
data = []
for i in range(1, 11):
    name = links[i].text
    magn = links[i]["href"]
    dict = {"name": name,
     "magnet":magn}
    data.append(dict)
header = data[1].keys()
with open("freinds.csv", "w", encoding="utf8", newline="") as f:
    write = csv.DictWriter(f, fieldnames=header)
    write.writeheader()
    write.writerows(data)
