import pandas as pd
import os

files = os.listdir(os.getcwd())

csvfiles = [f for f in files if f[-3:] == 'csv']

df = pd.concat((pd.read_csv(f) for f in csvfiles), ignore_index=True, sort=False)

item_pivot = pd.pivot_table(df, index=['Country', 'Item Type'], values=['Units Sold'], aggfunc=sum)
country_pivot = pd.pivot_table(df, index=['Item Type'], values=['Total Cost'], aggfunc=sum)
item_pivot.to_csv('item_pivot.csv')
country_pivot.to_csv('country_pivot.csv')
