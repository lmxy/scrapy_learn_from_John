# -*- coding = utf-8 -*-
# @Time : 2022/4/30 16:17
# @Author : yaowei
# @File : amz-reviews.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# url = 'https://www.amazon.com/Samsung-5100mAh-Battery-SM-T290-International/dp/B07XJZ7VQD/ref=sr_1_2?adgrpid=78907565662&gclid=Cj0KCQjwvLOTBhCJARIsACVldV0f7OVn2EHISJ2xfzXMW1mG2eAeoYEDL_gdjK7tEZ85S8gFxwepjBMaAuKHEALw_wcB&hvadid=393471688716&hvdev=c&hvlocphy=9040303&hvnetw=g&hvqmt=b&hvrand=18313933212484371634&hvtargid=kwd-297491522583&hydadcr=10782_10985474&keywords=%EC%95%84%EB%A7%88%EC%A1%B4&qid=1651307023&sr=8-2'
url = 'https://www.amazon.co.jp/dp/B08ZNJ9F4L?ref=emc_p_m_5_i&th=1'
# r = requests.get('http://localhost:8050'
#                  '/render.html', params={'url': url, 'wait': 2})
r = requests.get(url, headers=headers)
print(r)
print(r.text)




