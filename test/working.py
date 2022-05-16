# -*- coding = utf-8 -*-
# @Time : 2022/4/16 15:03
# @Author : yaowei
# @File : working.py
# @Software : PyCharm

import requests
import json

# url = "https://api.afl.com.au/cfs/afl/matchItem/CD_M20220140505"
url = "https://api.afl.com.au/statspro/playerStats/seasons/CD_S2020014"


headers = {
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'x-media-mis-token': '5fbb3a385dcdd702a8e6e8a8a70d2a3c',
  'Referer': 'https://www.afl.com.au/',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'Cookie': 'JSESSIONID=46C435A9389B77F18A3C740023229078'
}

r = requests.request("GET", url, headers=headers)

playerdata = r.json()



