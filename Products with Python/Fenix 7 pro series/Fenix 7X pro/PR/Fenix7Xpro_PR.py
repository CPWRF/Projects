# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
testresult = pd.read_excel('PR.xlsx',sheet_name='Test Result')
# %%
ProcessTypeBlackList = 'Pack|Click|RabbitCard|EasyCard|DeleteBundle|ProdScan|FileCopyer'
ItemNameBlackList = 'ESN|Check ProductionMap|Fixture ID|Battery Voltage'
def tweak(df):
    return(df
    .drop(columns='Comment')
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
raw = pd.read_excel('PR.xlsx', sheet_name='ASSY_Raw Data', usecols=["Item" + s for s in filter(testresult).Item.astype('str').to_list()]+['ItemNameType','Result','failitem'])
# %%
plt.style.use('fivethirtyeight')
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
my_hisplot(raw, 17788, 68, -30, "HT_GPS_L5 by ref (7x PRO)_16.06%")
# %%
my_hisplot(raw, 17788, 21, -30, "HT_GPS_L5 by ref (7 PRO)_12.16%")
# %%
my_hisplot(raw, 17937, 38, -30, "M_T_ANT_power 2450MHz BY REF (sapphire) (F7XPro)_6.07%")