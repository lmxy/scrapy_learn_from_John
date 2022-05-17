# -*- coding = utf-8 -*-
# @Time : 5/17/2022 10:51 PM
# @Author : yaowei
# @File : yt-address-csv-df.py
# @Software : PyCharm
import pandas as pd

df = pd.read_csv('address-data.csv')
pd.set_option('display.max_columns', None)

shipping_1day = df[df['Shipping Type'] == '1 Day']
shipping_2day = df[df['Shipping Type'] == '2 Day']
shipping_5day = df[df['Shipping Type'] == '5 Day']

# print(shipping_1day.head())
print(len(shipping_1day))
print(len(shipping_2day))
print(len(shipping_5day))
shipping_1day.to_csv('shipping-1.csv')