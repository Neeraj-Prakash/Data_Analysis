# Rolling Statistics and correlation Plot

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
style.use('fivethirtyeight')


HPI_data = pd.read_pickle('fiddy_states_pct.pickle')

fig = plt.figure()
ax1 = plt.subplot2grid((2,1) , (0,0))
ax2 = plt.subplot2grid((2,1) , (1,0), sharex=ax1)

##HPI_data['TX12MA'] = HPI_data['TX'].rolling(12).mean()
##HPI_data['TX12STD'] = HPI_data['TX'].rolling(12).std()
##
##print(HPI_data[['TX','TX12MA','TX12STD']].head())
##
##
##HPI_data[['TX','TX12MA']].plot(ax=ax1)
##HPI_data['TX12STD'].plot(ax=ax2)

TX_AK_12corr = HPI_data['TX'].rolling(12).corr(other=HPI_data['AK'])
HPI_data['TX'].plot(ax=ax1, label='TX HPI')
HPI_data['AK'].plot(ax=ax1, label='AK HPI')
ax1.legend()

TX_AK_12corr.plot(ax=ax2, label='TX_AK_12corr')

plt.legend()
plt.show()
