import requests
from bs4 import BeautifulSoup

url = 'https://www.skyports.com/premier-league-table'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
league_table = soup.find('table', class_='standing-table__table callfn')

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        position = row.find('td', class_='standing-table__cell').text
        team = row.find('td', class_='standing-table__cell standing-table__cell--name').text
        points = row.find_all('td', class_='standing-table__cell')[9].text
        print(position, team, points)