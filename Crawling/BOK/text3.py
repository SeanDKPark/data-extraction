import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bok_df = pd.read_csv('result_edit.csv').drop(columns = ['URL'])
bok_df['Date'] = pd.to_datetime(bok_df['Date'], format='%Y.%m.%d')
bok_df['Volume'] = bok_df['Volume'].str.replace(',', '').astype(int)

data = {
    'Date': [
        '2013-5-7', '2015-7-24', '2016-7-22', '2017-7-22', '2018-5-21',
        '2019-8-2', '2020-3-17', '2020-4-30', '2020-7-3', '2020-9-23',
        '2021-3-25', '2021-7-24', '2022-2-21', '2022-5-30'
    ],
    'Budget': [
        17.4, 11.6, 11.0, 11.0, 3.8, 5.8, 11.7, 12.2, 35.1, 7.8, 14.9, 34.9, 16.9, 62.0
    ]
}
budget_df = pd.DataFrame(data)
budget_df['Date'] = pd.to_datetime(budget_df['Date'])
budget_df['Budget'] = budget_df['Budget'] * 1000

kbond3_df = pd.read_csv('3year.csv').drop(columns = ['시가', '고가', '저가', '변동 %'])
kbond3_df['Date'] = pd.to_datetime(kbond3_df['날짜'].str.replace(' ', '', regex=False), format='%Y-%m-%d')
kbond3_df['3year_rate'] = kbond3_df['종가']
kbond3_df = kbond3_df.drop(columns = ['날짜', '종가'])

kbond10_df = pd.read_csv('10year.csv').drop(columns = ['시가', '고가', '저가', '변동 %'])
kbond10_df['Date'] = pd.to_datetime(kbond10_df['날짜'].str.replace(' ', '', regex=False), format='%Y-%m-%d')
kbond10_df['10year_rate'] = kbond10_df['종가']
kbond10_df = kbond10_df.drop(columns = ['날짜', '종가'])

'''
bokdata_df = pd.read_csv('bok_data.csv', encoding = 'utf-8')
df_dropped = bokdata_df.drop(columns=['통계표', '단위'])

df_melted = pd.melt(df_dropped, id_vars=['계정항목'], var_name='Period', value_name='Value')
df_melted = df_melted.drop(index = [0, 1])
print(df_melted)
df_melted['계정항목'] == '국채'

def assign_values(row):
    if row['계정항목'].strip(' ') == '국채':
        return pd.Series({'bonds_held': row['Value'], 'rp_sold': np.nan})
    elif row['계정항목'].strip(' ') == '환매조건부채권매각':
        return pd.Series({'bonds_held': np.nan, 'rp_sold': row['Value']})
    else:
        return pd.Series({'bonds_held': np.nan, 'rp_sold': np.nan})

df_melted[['bonds_held', 'rp_sold']] = df_melted.apply(assign_values, axis=1)
df_reasons = df_melted.drop(columns = ['계정항목'])


def quarter_end_date(period):
    year, quarter = period.split('/Q')
    year = int(year)
    quarter = int(quarter)

    # Map each quarter to its end date
    if quarter == 1:
        return pd.Timestamp(year=year, month=3, day=31)
    elif quarter == 2:
        return pd.Timestamp(year=year, month=6, day=30)
    elif quarter == 3:
        return pd.Timestamp(year=year, month=9, day=30)
    elif quarter == 4:
        return pd.Timestamp(year=year, month=12, day=31)
    else:
        raise ValueError(f"Invalid quarter: {quarter}")

df_reasons['Date'] = df_reasons['Period'].apply(quarter_end_date)
df_reasons = df_reasons.drop(columns = ['Period', 'Value'])

merged_df = pd.merge(bok_df, df_reasons, on='Date', how='outer')
merged_df['Date'] = pd.to_datetime(merged_df['Date'])

merged_df['bonds_held'] = pd.to_numeric(merged_df['bonds_held'].str.replace(',', ''), errors='coerce')  # Remove commas
merged_df['rp_sold'] = pd.to_numeric(merged_df['rp_sold'].str.replace(',', ''), errors='coerce')  # Remove commas

print(merged_df.head(100))

bonds_held_df = merged_df[['Date', 'bonds_held']].dropna(subset=['bonds_held'])
rp_sold_df = merged_df[['Date', 'rp_sold']].dropna(subset=['rp_sold'])

fig, ax = plt.subplots(figsize = (12, 6))

ax.bar(merged_df['Date'], merged_df['Volume'], width = 10, color='blue', label='BOK Outright Purchase')
ax.set_xlabel('Date')
ax.set_ylabel('Volume')
ax.legend(loc='upper left')

ax2 = ax.twinx()
ax2.step(bonds_held_df['Date'], bonds_held_df['bonds_held'], color = 'black', label = 'K Bonds held by BOK')
ax2.step(rp_sold_df['Date'], rp_sold_df['rp_sold'], color = 'grey', label = 'RP sold by BOK')
ax2.set_ylabel('End of the Quarter Balance')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('chart1.png')
plt.show()
'''


merged_df = pd.merge(bok_df, budget_df, on='Date', how='outer')
merged_df = pd.merge(merged_df, kbond10_df, on='Date', how='outer')
merged_df = pd.merge(merged_df, kbond3_df, on='Date', how='outer')

print(merged_df)

fig, ax = plt.subplots(figsize = (12, 6))

ax.bar(merged_df['Date'], merged_df['Volume'], width = 10, color='blue', label='BOK Outright Purchase')
ax.bar(merged_df['Date'], merged_df['Budget'], width = 10, color='red', label='Supplementary Budget')
ax.set_xlabel('Date')
ax.set_ylabel('Volume and Budget')
ax.legend(loc='upper left')

ax2 = ax.twinx()
ax2.plot(merged_df['Date'], merged_df['10year_rate'], color = 'black', label = '10 year K bond rate')
ax2.plot(merged_df['Date'], merged_df['3year_rate'], color = 'grey', label = '3 year K bond rate')

ax2.set_ylabel('K bond rate (%)')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('chart3.png')
plt.show()
