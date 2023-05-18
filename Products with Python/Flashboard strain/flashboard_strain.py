#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# %%
small = pd.read_excel('012-0452x-FF strain.xlsx', sheet_name='012-04522-FF')
mid = pd.read_excel('012-0452x-FF strain.xlsx', sheet_name='012-04523-FF')
# %%
plt.figure(dpi=150)
pd.merge(left=small,right=mid,how='outer', on='Time(sec)').set_index('Time(sec)').plot()
plt.title('Flashlight board assy strain_h-axis')
plt.ylabel('Strain(um/m)')