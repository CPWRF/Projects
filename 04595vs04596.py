# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%
small = pd.read_excel('04595vs04596.xlsx', sheet_name='04595')
mid = pd.read_excel('04595vs04596.xlsx', sheet_name='04596')
# %%
merged = pd.merge(left=small, right=mid, left_on='time',right_on='time').set_index('time')
# %%
plt.style.use('fivethirtyeight')
# %%
merged.plot(figsize=(15,10))
plt.text(x=-1, y=10, s='Before\nput into\nhousing')
plt.text(x=48, y=10, s='After\nscrew')
plt.ylim(-500,500)
plt.title("Screw MB manually w/o fixture")