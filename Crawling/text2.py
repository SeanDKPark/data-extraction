import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df_sell = pd.read_csv('rp_sell.csv', encoding = 'utf-8')
df_buy = pd.read_csv('rp_buy.csv', encoding = 'utf-8')

print(df_sell.head())
print(df_sell.shape)

print(df_buy.head())
print(df_buy.shape)