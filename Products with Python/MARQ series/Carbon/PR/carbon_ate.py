#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
plt.style.use("fivethirtyeight")
data = pd.read_csv('carbon_ft2.csv')
# %%
def tweak_data(data):
    return(data
    .query("ItemNameType == 15689 & failitem.isin([0,203])")
    )
# %%
plt.figure(dpi=150)
sns.histplot(data=tweak_data(data), x='Item203', hue='Result', hue_order=[1,0], kde=True)
plt.title("FT2_ANT Power")