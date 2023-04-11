# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
testresult = pd.read_excel('45_raw_FP.xlsx',sheet_name='Test Result')
# %%
ProcessTypeBlackList = 'Pack|Click|RabbitCard|EasyCard|DeleteBundle|ProdScan|FileCopyer'
ItemNameBlackList = 'ESN|Check ProductionMap|Fixture ID|RGN'
def tweak(df):
    return(df
    .drop("Comment",axis=1)
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
#%%
filter(testresult).query("ItemName.str.contains('GPS')")
# %%
raw = pd.read_excel('tweak_raw.xlsx')
# raw = pd.read_excel('45_raw_FP.xlsx', sheet_name='Raw Data', usecols=["Item" + s for s in filter(testresult).Item.astype('str').to_list()]+['ItemNameType','Result','failitem'])
# %%
def tweak_df(df,itemnametype, item, lower):    
    return(df
    .query(f"ItemNameType=={itemnametype} and failitem.isin([0,{item}]) and Item{item}>{lower}")
    [['Result',f'Item{item}']]
    )
def my_hisplot(df,itemnametype, item, lower, title):
    print(f"{ppk_df(df,itemnametype, item).agg(['min','max'])}")
    plt.figure(dpi=100)
    plt.title(title)
    sns.histplot(data = (tweak_df(df,itemnametype, item, lower))
    ,x=f'Item{item}'
    ,hue='Result'
    ,hue_order=[1,0])
def ppk_df(df,itemnametype, item):
    return(df
    .query(f"ItemNameType=={itemnametype} and Result==True")
    [f'Item{item}']
    )
def ppk_result(df, upper, lower):
    pp = mn.calc_pp(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    ppk = mn.calc_ppk(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    sugg = mn.suggest_specification_limits(df)
    print(f"ppk={ppk}, pp={pp}, sugg={sugg}")
# %%
plt.style.use('fivethirtyeight')
# %%
my_hisplot(raw,17993,89,-20,"HT_GPS Radiated Sensitivity_3.31%");
# %%
my_hisplot(raw,17992,89,-20,"CT_GPS Radiated Sensitivity non_recheck_2.25%");
# %%
my_hisplot(raw,17997,89,-20,"FT1_GPS Radiated Sensitivity_1.84%");
#%%
my_hisplot(raw,17994,89,-20,"RT1_GPS Radiated Sensitivity_1.2%");