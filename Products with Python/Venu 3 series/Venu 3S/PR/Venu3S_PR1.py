# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
testresult = pd.read_excel('Venu3S_PR1_45.xlsx',sheet_name='Test Result')
# %%
ProcessTypeBlackList = 'Pack|Click|RabbitCard|EasyCard|DeleteBundle|ProdScan|FileCopyer'
ItemNameBlackList = 'ESN|Check ProductionMap|Fixture ID|Battery Voltage'
def tweak(df):
    return(df
    # .drop(columns='Comment')
    .rename(columns = lambda name : name.replace(" ",'').replace('/','').replace('%',''))
    .sort_values('Retest', ascending=False)
    .astype({'ItemNameType':'category','ProcessType':'category','Item':'category','ItemName':'category'})
    .assign(CountESN = lambda df : df.CountCountESN.str.split('/').str[1].astype('int16'))
    .query("~ProcessType.str.contains(@ProcessTypeBlackList) and ~ItemName.str.contains(@ItemNameBlackList)"))
def filter(df):
    return(tweak(df)
    .query("CountESN > CountESN.quantile(0.07)")
    .query("Retest >= Retest.mean()"))
def degree(df):
    return(tweak(df)
    .Retest.mean().round(2))
filter(testresult)
# %%
# filter(testresult).to_excel(f'Triggerby{degree(testresult)}percent.xlsx', index=False)
# %%
raw = pd.read_excel('Venu3S_PR1_raw.xlsx')
# %%
plt.style.use('fivethirtyeight')
# def tweak_df(df,itemnametype, item, lower):    
#     return(df
#     .query(f"ItemNameType=={itemnametype} and failitem.isin([0,{item}]) and Item{item}>{lower}")
#     [['Result',f'Item{item}']]
#     )
# def my_hisplot(df,itemnametype, item, lower, title):
#     print(f"{ppk_df(df,itemnametype, item).agg(['min','max'])}")
#     plt.figure(dpi=100)
#     plt.title(title)
#     sns.histplot(data = (tweak_df(df,itemnametype, item, lower))
#     ,x=f'Item{item}'
#     ,hue='Result'
#     ,hue_order=[1,0])
def ppk_df(df,itemnametype, item):
    return(df
    .query(f"ItemNameType=={itemnametype} and Item{item}St==1")
    [f'Item{item}']
    )
def ppk_result(df, upper, lower):
    pp = mn.calc_pp(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    ppk = mn.calc_ppk(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    sugg = mn.suggest_specification_limits(df)
    print(f"ppk={ppk}, pp={pp}, sugg={sugg}")
#%%
def my_hisplot_SQL(df,itemnametype, item, lower,title):
    # print(f"{ppk_df(df,itemnametype, item).agg(['min','max'])}")
    plt.figure(dpi=100)
    plt.title(title)
    sns.histplot(data = raw.query(
        f"ItemNameType == {itemnametype} and Item{item}St.isin([0,1]) and Item{item}>{lower}")
    ,x=f'Item{item}'
    ,hue=f'Item{item}St'
    ,hue_order=[1,0])

def my_hisplot_SQL2(df,itemnametype, item, lower,title):
    plt.figure(dpi=100)
    plt.title(title)
    sns.histplot(data = raw
                 .query(f"ItemNameType == {itemnametype} and Item{item}>{lower}")
                 .assign(Item27 = df.Item27.clip(-10))
    ,x=f'Item{item}'
    ,hue=f'Item{item}St')
# %%
ECG_RT = 16593
AutoCT = 16578
RTESN = 16954
RST = 17111
# %%
my_hisplot_SQL(raw, ECG_RT, 11, -999, "ECG_RT_ECG impedance short")
# %%
my_hisplot_SQL(raw, AutoCT, 27, -999, "AutoCT_Barometer Temperature")
# %%
my_hisplot_SQL(raw, RTESN, 27, -999, "RTESN_CNo")
#%%
my_hisplot_SQL2(raw, RTESN, 27, -1000, "RTESN_CNo")
# %%
my_hisplot_SQL(raw, RST, 15, -999, "RST_[Diff]Speaker 1000Hz")
# %%
my_hisplot_SQL(raw, ECG_RT, 31, 1, "ECG_RT_ECG 2mv 1Hz Test")
# %%
mn.ppk_plot(ppk_df(raw, 16579,42), upper_specification_limit=1.5, lower_specification_limit=-1.5)
# %%
ppk_df(raw, 16578,46).agg(['max','min'])
#%%
mn.ppk_plot(ppk_df(raw, 16578,46), upper_specification_limit=1.5, lower_specification_limit=-1.5)
#%%
ppk_df(raw, 16585,89).agg(['max','min'])
# %%
mn.ppk_plot(ppk_df(raw, 16585,89), upper_specification_limit=1.5, lower_specification_limit=-1.5)
# %%
