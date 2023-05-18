#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
Formal_CT = pd.read_excel('FormalTest_CT.xlsx')
QA_CT = pd.read_excel('QAtest_CT.xlsx')
# %%
CT = pd.merge(left=QA_CT, right=Formal_CT, 
         left_on=['SerialNumber','ItemNameType'], 
         right_on=['SerialNumber','ItemNameType'],
         suffixes=['_QA','_Formal'])
# %%
sns.violinplot(data=CT.iloc[:,2:])
plt.title('CT')
#%%
Formal_FT = pd.read_excel('FormalTest_FT.xlsx')
QA_FT = pd.read_excel('QAtest_FT.xlsx')
# %%
FT = pd.merge(left=QA_FT, right=Formal_FT, 
         left_on=['SerialNumber','ItemNameType'], 
         right_on=['SerialNumber','ItemNameType'],
         suffixes=['_QA','_Formal'])
# %%
sns.violinplot(data=FT.iloc[:,2:])
plt.title('FT')