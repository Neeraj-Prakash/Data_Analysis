# Reading data from csv file and editing

import pandas as pd
df = pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv')

print(df.head())
print()

df.set_index('Date',inplace=True)
#print(df.head())
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())
print()

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv', header=False)

df = pd.read_csv('newcsv4.csv',names=['Date','Austin_HPI'],index_col=0)
print(df.head())

df.to_html('example.html')

df = pd.read_csv('newcsv4.csv',names=['Dates','Austin_HPI'])
print(df.head())
df.rename(columns={'Austin_HPI':'77006_HPI'},inplace=True)
print(df.head())

