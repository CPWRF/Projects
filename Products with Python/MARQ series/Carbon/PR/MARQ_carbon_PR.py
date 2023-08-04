# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# testresult = pd.read_excel('MARQ_carbon_PR.xlsx')
# %%
# ProcessTypeBlackList = 'Pack|Click|RabbitCard|EasyCard|DeleteBundle|ProdScan|FileCopyer'
# ItemNameBlackList = 'ESN|Check ProductionMap|Fixture ID|Battery Voltage'
# def tweak(df):
#     return(df
#     # .drop(columns='Comment')
#     .rename(columns = lambda name : name.replace(" ",'').replace('/','').replace('%',''))
#     .sort_values('Retest', ascending=False)
#     .astype({'ItemNameType':'category','ProcessType':'category','Item':'category','ItemName':'category'})
#     .assign(CountESN = lambda df : df.CountCountESN.str.split('/').str[1].astype('int16'))
#     .query("~ProcessType.str.contains(@ProcessTypeBlackList) and ~ItemName.str.contains(@ItemNameBlackList)"))
# def filter(df):
#     return(tweak(df)
#     .query("CountESN > CountESN.quantile(0.07)")
#     .query("Retest >= Retest.mean()"))
# def degree(df):
#     return(tweak(df)
#     .Retest.mean().round(2))
# filter(testresult)
# %%
# filter(testresult).to_excel(f'Triggerby{degree(testresult)}percent.xlsx', index=False)
# %%
raw = pd.read_excel('MARQ_carbon_PR.xlsx')
# %%
plt.style.use('fivethirtyeight')
def tweak_df(df,itemnametype, item, lower):    
    return(df
    .query(f"ItemNameType=={itemnametype} and failitem.isin([0,{item}]) and Item{item}>{lower}")
    [['Result',f'Item{item}']]
    )
def my_hisplot(df,itemnametype, item, lower, title):
    plt.figure(dpi=100)
    plt.title(title)
    sns.histplot(data = (tweak_df(df,itemnametype, item, lower))
    ,x=f'Item{item}'
    ,hue='Result'
    ,hue_order=[1,0])
#%%
# def my_hisplot_SQL(df,itemnametype, item, lower,title):
#     # print(f"{ppk_df(df,itemnametype, item).agg(['min','max'])}")
#     plt.figure(dpi=100)
#     plt.title(title)
#     sns.histplot(data = raw.query(
#         f"ItemNameType == {itemnametype} and Item{item}St.isin([0,1]) and Item{item}>{lower}")
#     ,x=f'Item{item}'
#     ,hue=f'Item{item}St'
#     ,hue_order=[1,0])

# def my_hisplot_SQL2(df,itemnametype, item, lower,title):
#     plt.figure(dpi=100)
#     plt.title(title)
#     sns.histplot(data = raw
#                  .query(f"ItemNameType == {itemnametype} and Item{item}>{lower}")
#                  .assign(Item27 = df.Item27.clip(-10))
#     ,x=f'Item{item}'
#     ,hue=f'Item{item}St')
# %%
AutoATE = 15545
# %%
my_hisplot(raw, AutoATE, 143, 0, "ECG_RT_ECG impedance short")
plt.xlim([0,1])