# Adding variables in the dataset and visualizing the data

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
style.use('fivethirtyeight')

##def state_list():
##    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
##    return fiddy_states[0][1][1:]
##states = state_list()
##for abbv in states:
##    HPI_data[abbv] = (HPI_data[abbv] - HPI_data[abbv][0]) / HPI_data[abbv][0] *100.0
##

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA')
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] *100.0
    return df

HPI_data = pd.read_pickle('fiddy_states_pct.pickle')


##benchmark = HPI_Benchmark()
##
##fig = plt.figure()
##ax1 = plt.subplot2grid((1,1),(0,0))
##
##HPI_data.plot(ax = ax1)
##benchmark.plot(ax=ax1, color='k', linewidth=10)
##
##plt.legend().remove()
##plt.show()

HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)
print(HPI_State_Correlation.describe())
