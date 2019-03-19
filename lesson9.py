# Resampling Data

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
style.use('fivethirtyeight')


HPI_data = pd.read_pickle('fiddy_states_pct.pickle')

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

#Resampling the mothly data to annualy
TX1yr = HPI_data['TX'].resample('A').mean()
print(TX1yr.head())

HPI_data['TX'].plot(ax=ax1, label = 'Monthly TX  HPI')
TX1yr.plot(ax = ax1, label = 'Yearly TX HPI')

plt.legend()
plt.show()

