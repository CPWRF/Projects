#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
raw = pd.read_excel('Alpha LTE Item22.xlsx')
#%%
plt.style.use('fivethirtyeight')
sns.violinplot(data=raw, x='StationID', y='Item22', inner=None)
sns.swarmplot(data=raw, x='StationID', y='Item22', color='white')
#%%
