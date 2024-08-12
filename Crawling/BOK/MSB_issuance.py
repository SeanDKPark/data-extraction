import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

def classify_code(code):
    if re.match(r'DC\d{2,3}-\d{4}-\d{4}', code):
        return '<1y'
    elif re.match(r'\d{4,5}-\d{4}-01\d{2}', code):
        return '1y'
    elif re.match(r'\d{4,5}-\d{4}-02\d{2}', code):
        return '2y'
    elif re.match(r'\d{4,5}-\d{4}-03\d{2}', code):
        return '3y'
    else:
        return 'Unknown'

df_issue = pd.read_excel('MSB_issue_data.xls', header = 1)

print(df_issue.head())

# Auctions info

df_auctions = pd.read_csv('MSB_auctions_data.csv').iloc[:838, :] #14년도부터
test_df = df_auctions.iloc[:, :]
m, n = test_df.shape

# Define the regular expression pattern
isin_pattern = re.compile(r'물\(([^)]+)\)')
bid_pattern = re.compile(r'응찰액\(응찰기관수\):(\d+\.\d+)|응찰액:(\d+\.\d+)')
planned_pattern = re.compile(r'발행예정액:(\d+\.\d+)')
covered_pattern = re.compile(r'낙찰액\(낙찰기관수\):(\d+\.\d+)|낙찰액:(\d+\.\d+)')
year_pattern = re.compile(r'\b\d{4}\b')

result_dfs = []

for i in range(m):
    title = test_df['Titles'].iloc[i]
    text = test_df['Text'].iloc[i].replace(' ', '')
    isins = isin_pattern.findall(text)
    bids_matches = bid_pattern.findall(text)
    bids_str = [match for match_tuple in bids_matches for match in match_tuple if match]
    planneds_str = planned_pattern.findall(text)
    covereds_matches = covered_pattern.findall(text)
    covereds_str = [match for match_tuple in covereds_matches for match in match_tuple if match]
    bids = [float(item) for item in bids_str]
    planneds = [float(item) for item in planneds_str]
    covereds = [float(item) for item in covereds_str]
    years = [int(item) for item in year_pattern.findall(title)] * len(isins)
    # if len(bids) == 0:
    #     print(test_df['Text'].iloc[i])
    #     print('!!!')
    # if len(bids) != len(isins):
    #     print(test_df['Text'].iloc[i])
    #     print('@@@')
    # if len(bids) != len(vols):
    #     print(test_df['Text'].iloc[i])
    #     print('###')
    result_df = pd.DataFrame({
        'isin' : isins,
        'bid': bids,
        'covered': covereds,
        'planned' : planneds,
        'issued_year' : years
    })
    result_dfs.append(result_df)

auctions_df = pd.concat(result_dfs, ignore_index = True)
auctions_df['maturity'] = auctions_df['isin'].apply(classify_code)

# Tenders info

df_tenders = pd.read_csv('MSB_tenders_data.csv').iloc[:127, :] #14년도부터
test_df = df_tenders.iloc[:, :]
m, n = test_df.shape

isin_pattern = re.compile(r'\d{4,5}-\d{4}-\d{4}')
bid_pattern = re.compile(r'응모액:\d+\.\d+조원\(.*?(\d+\.\d+)조원,.*?(\d+\.\d+)조원\)')
planned_pattern = re.compile(r'모집예정액:\d+\.\d+조원\(.*?(\d+\.\d+)조원,.*?(\d+\.\d+)조원\)')
covered_pattern = re.compile(r'낙찰액:\d+\.\d+조원\(.*?(\d+\.\d+)조원,.*?(\d+\.\d+)조원\)')
year_pattern = re.compile(r'\b\d{4}\b')

result_dfs = []

for i in range(m):
    title = test_df['Titles'].iloc[i]
    text = test_df['Text'].iloc[i].replace(' ', '')
    substrings = text.split('년물')

    isins = []
    covereds = []
    planneds = []
    bids = []
    years = []
    for substr in substrings[1:]:
        isins.extend(isin_pattern.findall(substr))
        covereds.extend(covered_pattern.findall(substr))
        planneds.extend(planned_pattern.findall(substr))
        bids.extend(bid_pattern.findall(substr))
    years = [int(item) for item in year_pattern.findall(title)] * len(isins)
    covereds_flat = [float(item) for sublist in covereds for item in sublist]
    planneds_flat = [float(item) for sublist in planneds for item in sublist]
    bids_flat = [float(item) for sublist in bids for item in sublist]

    result_df = pd.DataFrame({
        'isin' : isins,
        'bid' : bids_flat,
        'covered' : covereds_flat,
        'planned' : planneds_flat,
        'issued_year' : years
    })
    result_dfs.append(result_df)

tenders_df = pd.concat(result_dfs, ignore_index = True)
tenders_df['maturity'] = tenders_df['isin'].apply(classify_code)

final_df = pd.concat([auctions_df, tenders_df], axis = 0, ignore_index = True)
print(final_df)

# Weighted Average BtC Rates

def weighted_avg(df):
    return df['bid'].sum() / df['covered'].sum()

bid_rate_df = final_df.groupby(['issued_year', 'maturity']).apply(weighted_avg).reset_index(name='weighted_avg_bid_rate')


final_df['failure'] = (final_df['bid'] < final_df['planned']).astype(int)

print(final_df)

def sum_of_failures(df):
    return df['failure'].sum()

def failure_rate(df):
    return 100 * df['failure'].sum() / df.shape[0]

failures_df = final_df.groupby(['issued_year', 'maturity']).apply(sum_of_failures).reset_index(name= 'sum_of_failures')
print(failures_df)
failures_df.to_excel('failures.xlsx')

failure_rate_df = final_df.groupby(['issued_year', 'maturity']).apply(failure_rate).reset_index(name= 'failure_rate')
print(failure_rate_df)
failure_rate_df.to_excel('failure_rate.xlsx')

fig, ax = plt.subplots()
for maturity in ['<1y', '1y', '2y', '3y']:
    subset = bid_rate_df[bid_rate_df['maturity'] == maturity]
    ax.plot(subset['issued_year'], subset['weighted_avg_bid_rate'], marker='o', label=maturity)

ax.set_title('Weighted Average Bid to Cover Rate')
ax.set_xlabel('Issued Year')
ax.set_ylabel('Weighted Average Bid to Cover Rate')
ax.legend(title='Maturity')
ax.grid(True)
ax.set_xticks(bid_rate_df['issued_year'].unique())  # Ensure all years are shown

plt.tight_layout()  # Adjust layout to fit all elements
plt.savefig('MSB_btc_rate.png')
plt.show()

bid_rate_df.to_excel('bid_rate_df.xlsx')

# Cumulative Covered Chart

# Group by 'issued_year' and 'maturity' and calculate the sum of 'covered'
grouped = final_df.groupby(['issued_year', 'maturity'])['covered'].sum().reset_index(name='sum_of_covered')

grouped['total_covered'] = grouped.groupby('issued_year')['sum_of_covered'].transform('sum')
grouped['percentage'] = grouped['sum_of_covered'] / grouped['total_covered'] * 100

print(grouped)

pivot_df = grouped.pivot_table(index='issued_year', columns='maturity', values='percentage', fill_value=0)

desired_order = ['<1y', '1y', '2y', '3y']
pivot_df = pivot_df[desired_order]

print(pivot_df)

total_covered_by_year = grouped.groupby('issued_year')['total_covered'].first()

# Plotting
fig, ax1 = plt.subplots()

# Create a stacked area plot
pivot_df.plot(kind='area', stacked=True, ax=ax1, colormap='viridis', alpha=0.7)

ax1.set_xticks(np.arange(2014, 2025, 1))
ax1.set_xlabel('Issued Year')
ax1.set_ylabel('Cumulative Percentage (%)')
ax1.legend(title='Maturity', loc='lower left')
ax1.grid(True)
ax1.set_xlim([pivot_df.index.min(), pivot_df.index.max()])
ax1.set_ylim([0, 100])

ax2 = ax1.twinx()
ax2.plot(total_covered_by_year.index, total_covered_by_year.values, color='black', marker='o', linestyle='-', linewidth=2, label='Total Covered')
ax2.set_xlabel('Issued Year')
ax2.set_ylabel('Total MSBs Issued')
ax2.legend()

fig.suptitle('MSB Issuance (~Jul-24)')

# Show the plot
plt.tight_layout()
plt.savefig('MSB_covered_time_series.png')
plt.show()