# encoding='UTF-8'
import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
# page = 1
# url = f'https://sukebei.nyaa.si/?f=2&c=1_1&q=%5BSakuraCircle%5D&p={page}'
url = 'https://sukebei.nyaa.si/?f=2&c=1_1&q=%5BSakuraCircle%5D'
# r = requests.get(url=url, headers=headers)

with open('nyaa.html', 'r', encoding='utf8') as f:
    r = f.read()

# print(r)
soup = BeautifulSoup(r, 'lxml')
data = soup.select('tbody > tr ')

dl = {}
wr = []
for x in data:
    name = x.select('tr > td:nth-child(2) > a:nth-child(2)')[0].text
    magnet = x.select('tr > td:nth-child(3) > a:nth-child(2)')['href']
    dl = {
        'name': name,
        'magnet': magnet
    }
    wr.append(dl)
df = pd.DataFrame(wr)
df.to_excel('nyaa.xlsx', index=False)
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


