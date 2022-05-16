# -*- coding = utf-8 -*-
# @Time : 2022/4/17 20:12
# @Author : yaowei
# @File : readhtml.py
# @Software : PyCharm
import csv

import pandas as pd

# url = 'https://nyaa.si/?f=0&c=0_0&q=erai-raws+1080'
url = 'https://nyaa.si/?f=0&c=0_0&q=%5BSubsPlease%5D++1080'
table = pd.read_html(url)[0]


# table.to_excel('erai.xlsx')
table.to_excel('SupPlease.xlsx')
