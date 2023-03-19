# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
testresult = pd.read_excel('fenix 7S Pro_45_raw_PR.xlsx',sheet_name='Test Result')
# %%
ProcessTypeBlackList = 'Pack|Click|RabbitCard|EasyCard|DeleteBundle|ProdScan|FileCopyer'
ItemNameBlackList = 'ESN|Check ProductionMap|Fixture ID'
def filter(df):
    return(df
    .rename(columns = lambda name : name.replace(" ",'').replace('/','').replace('%',''))
    .sort_values('Retest', ascending=False)
    .astype({'ItemNameType':'category','ProcessType':'category','Item':'category','ItemName':'category'})
    .assign(CountESN = lambda df : df.CountCountESN.str.split('/').str[1].astype('int16'))
    .query("~ProcessType.str.contains(@ProcessTypeBlackList) and ~ItemName.str.contains(@ItemNameBlackList)")
    # .CountESN.quantile(0.03)
    .query("CountESN > CountESN.quantile(0.05)")
    .query("Retest >= Retest.mean()")
    # .Retest.mean()
    )
filter(testresult)
# %%
filter(testresult).query("ItemName.str.contains('ref') or ItemName.str.contains('REF')")
# %%
raw = pd.read_excel('fenix 7S Pro_45_raw_PR.xlsx',sheet_name='Rawdata')
# %%
def tweak_df(df,itemnametype, item, lower):    
    return(df
    .query(f"ItemNameType=={itemnametype} and failitem.isin([0,{item}]) and Item{item}>{lower}")
    [['ProcessType','Result',f'Item{item}','JobNO','StationID','Station']]
    .astype({'JobNO':'category'})
    .sort_values('JobNO', ascending=False)
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
    ppk = mn.calc_ppk(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    pp = mn.calc_pp(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    sug_lower, sug_upper = mn.suggest_specification_limits(df)
    print(f"ppk={ppk}, pp={pp}, sug_lower={sug_lower.round(2)}, sug_upper={sug_upper.round(2)}")
# %%
plt.style.use('fivethirtyeight')
# %%
my_hisplot(raw,17937,21,-20, 'M_T_ANT_power 2450MHz BY REF (sapphire) (F7sPro)_13.62%');
# 1. 校驗時ITMXP沒抓到Golden值，所以DUT的byRef值會遠高於golden 
# 2. 導入治具底板，確保各治具間間隔
# 3. 2.4G彈片被折斷 & 爬到板子上
# %%
my_hisplot(raw,17788,42,-20, 'HT_GPS_L5 by ref_5.37%');
# %%
my_hisplot(raw,17936,12,-20, 'FT1_GPS_ (L1 + L5) by ref(Glass)_5.34%');
#%%
my_hisplot(raw.query("Item60 != 0"),17787,60,-20, 'CT_GPS_ (L1 + L5) by ref_2.41%');
# 以上三項要再請教Sam黃
# %%
ppk_result(ppk_df(raw,17937,21), lower=ppk_df(raw,17937,21).min(), upper=ppk_df(raw,17937,21).max())
# %%
ppk_result(ppk_df(raw,17788,42), lower=-3.5, upper=2.5)
# %%
ppk_result(ppk_df(raw,17936,12), lower=-2.5, upper=1.5)
# %%
ppk_result(ppk_df(raw,17787,60), lower=-2, upper=2)
