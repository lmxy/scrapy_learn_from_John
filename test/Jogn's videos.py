# -*- coding = utf-8 -*-
# @Time : 2022/4/30 16:59
# @Author : yaowei
# @File : Jogn's videos.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import csv

def request():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    url = 'https://www.youtube.com/c/JohnWatsonRooney/videos'
    # url = 'https://www.google.com'
    response = requests.get(url, headers=headers)
    return  response.content


def parse(r):
    # with open('John videos.html', 'rb') as f:
    #     r = f.read()

    soup = BeautifulSoup(r, 'html.parser')
    container = soup.select('h3.style-scope.ytd-grid-video-renderer > a')
    list = []

    for i in container:
        title = i.text
        views = i['aria-label'].split(' ', 100)[-1]
        duration = i['aria-label'].split(' ', 100)[-2]
        after_uploaded = i['aria-label'].split(' ', 100)[-3]
        author = i['aria-label'].split(' ', 100)[-6][2:] + ' ' + i['aria-label'].split(' ', 100)[-5] + ' ' + i['aria-label'].split(' ', 100)[-4]
        link = 'https://www.youtube.com' + i['href']
        data = {
            'title': title,
            'author': author,
            'after_uploaded': after_uploaded,
            'duration': duration,
            'link': link
        }
        list.append(data)

    return list

def save(list):
    header = list[0].keys()

    with open('John_videos_list.csv', 'w', encoding='UTF8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(list)


if __name__ == '__main__':
    r = request()
    print(r)
    # list = parse(r)
    # save(list)