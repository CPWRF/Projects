#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
pre = pd.read_excel('FFP.xlsx', sheet_name='Test Result')
next = pd.read_excel('PR.xlsx', sheet_name='45')

ProcessTypeBlackList = 'Pack|Click|RabbitCard|EasyCard|DeleteBundle|ProdScan|FileCopyer'
ItemNameBlackList = 'ESN|Check ProductionMap|Fixture ID'

def tweak(raw):
    return(raw
    .drop('Comment',axis=1, errors='ignore')
    .rename(columns = lambda name : name.replace(" ",'').replace('/','').replace('%',''))
    .sort_values('Retest', ascending=False)
    .astype({'ItemNameType':'category','ProcessType':'category','Item':'category','ItemName':'category'})
    .assign(CountESN = lambda df : df.CountCountESN.str.split('/').str[1].astype('int16'))
    .query("~ProcessType.str.contains(@ProcessTypeBlackList) and ~ItemName.str.contains(@ItemNameBlackList)")
    )
def tweak_filter(raw):
    return(tweak(raw)
    # .query("CountESN > CountESN.quantile(0.05)")
    .query("Retest >= Retest.mean()")
    # .Retest.mean()
    )
# %%
pre_next = pd.merge(
    left=tweak_filter(pre), right=tweak(next), how='left',
    left_on=['ItemNameType','Item'], right_on=['ItemNameType','Item'],
    suffixes=['_pre','_next']).drop(columns=['ItemName_next','ProcessType_next'])
pre_next
# %%
# RetryImproveRate
def RetryImprove(df):
    return((100 * (df.Retest_pre.sum() - df.Retest_next.sum()) / df.Retest_pre.sum()).round(2))
RetryImprove(pre_next)
# %% 
def RetryDiff(df):
    return(df
     .assign(diff = df.Retest_pre - df.Retest_next)
     [['ProcessType_pre','ItemName_pre','diff']]
     .sort_values('diff', ascending=False)
     .dropna(axis=0)
     .style.bar('diff', color=['red','green'])
     )
RetryDiff(pre_next)
# %%
with pd.ExcelWriter(f"output_{RetryImprove(pre_next)}%improved.xlsx", engine='openpyxl') as writer:
    pre_next.to_excel(writer, sheet_name='Merge', index=False)
    RetryDiff(pre_next).to_excel(writer, sheet_name='RetryDiff', index=False)
    
#%%
# Total improvement rate
100*((tweak(pre).Retest.sum() - tweak(next).Retest.sum())/ tweak(pre).Retest.sum())