# -*- coding = utf-8 -*-
# @Time : 5/15/2022 3:45 PM
# @Author : yaowei
# @File : websraping-tables.py.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.skysports.com/premier-league-table'
url1 = 'https://www.skysports.com/championship-table'

def get_league_talbe(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    league_table = soup.find('table', class_='standing-table__table')
    tablelist = []

    for team in league_table.find_all('tbody'):
        rows = team.find_all('tr')
        for row in rows:
            pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
            pl_points = row.findAll('td')[9].text.strip()
            teamleague = {
                'name': pl_team,
                'points': pl_points
            }
            tablelist.append(teamleague)
    return tablelist

data = get_league_talbe(url)
df = pd.DataFrame(data)
df.to_csv('leaguetable.csv')
df.to_excel('leaguetable.xlsx')
print('saved to file')
