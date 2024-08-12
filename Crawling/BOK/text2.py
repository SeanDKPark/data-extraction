import pandas as pd
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df_sell = pd.read_csv('rp_sell.csv', encoding = 'utf-8')
df_buy = pd.read_csv('rp_buy.csv', encoding = 'utf-8')
df_outright = pd.read_csv('outright_transactions.csv', encoding = 'utf-8')

# print(df_sell.head())
# print(df_sell.shape)
#
# print(df_buy.head())
# print(df_buy.shape)

# print(df_outright)
# print(df_outright.shape)
# print(df_outright.columns)
# print(df_outright['Text'])

df_outright = df_outright.drop_duplicates()

m, n = df_outright.shape

date_pattern = r'\d{4}\.\d{1,2}\.\d{1,2}'
dates_list = []
for i in range(m):
    match = re.search(date_pattern, df_outright['Text'].iloc[i])
    if match:
        date = match.group()
        dates_list.append(date)
    else:
        dates_list.append('엥')
df_outright['Date'] = dates_list

volume_pattern = r'매입예정금액\(([\d,]+)억원\)'
volumes_list = []
for i in range(m):
    match = re.search(volume_pattern, df_outright['Text'].iloc[i])
    if match:
        volume = match.group(1)
        volumes_list.append(volume)
    else:
        volumes_list.append('엥')
df_outright['Volume'] = volumes_list

print(df_outright['Date'])
print(df_outright['Volume'])

df_outright[['Date', 'Volume', 'URL']].to_csv('result.csv', index = False )