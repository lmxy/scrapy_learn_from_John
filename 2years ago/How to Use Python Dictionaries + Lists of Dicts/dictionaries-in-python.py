# -*- coding = utf-8 -*-
# @Time : 5/17/2022 10:35 PM
# @Author : yaowei
# @File : dictionaries-in-python.py
# @Software : PyCharm

product = [
    {'itemid': '1001', 'name': 'tshirt', 'colour': 'white', 'size': ['small', 'medium', 'large']},
    {'itemid': '1002', 'name': 'sweatshirt', 'colour': 'black', 'size': ['medium', 'large', 'x-large']},
    {'itemid': '1003', 'name': 'hoody', 'colour': 'green', 'size': ['small', 'medium', 'large']}
]

print(product[0]['itemid'], product[0]['name'], product[0]['size'][0])