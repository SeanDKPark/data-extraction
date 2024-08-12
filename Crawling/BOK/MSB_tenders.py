import pandas as pd
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df_issue = pd.read_excel('MSB_issue_data.xls', header = 1)


print(df_issue)