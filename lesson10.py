# Handling missing Data in the data set

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
style.use('fivethirtyeight')


HPI_data = pd.read_pickle('fiddy_states_pct.pickle')

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

#Resampling the mothly data to annualy
HPI_data['TX1yr'] = HPI_data['TX'].resample('A').mean()
print(HPI_data[['TX','TX1yr']].head())

#HPI_data.dropna( inplace=True)
HPI_data.fillna(method='bfill',inplace=True)
print(HPI_data[['TX','TX1yr']].head())

HPI_data[['TX','TX1yr']].plot(ax=ax1)

plt.legend()
plt.show()
