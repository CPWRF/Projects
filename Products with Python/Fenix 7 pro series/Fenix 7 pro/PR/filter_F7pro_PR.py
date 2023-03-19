# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
testresult = pd.read_excel('Fenix7pro_PR_45_raw.xlsx',sheet_name='Test Result')
# %%
ProcessTypeBlackList = 'Pack|Click|RabbitCard|EasyCard|DeleteBundle|ProdScan|FileCopyer'
ItemNameBlackList = 'ESN|Check ProductionMap|Fixture ID'
def filter(raw):
    return(raw
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
raw = pd.read_excel('Fenix7pro_PR_45_raw.xlsx',sheet_name='PR_Raw Data')
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
    return(sns.histplot(data = (tweak_df(df,itemnametype, item, lower))
    ,x=f'Item{item}'
    ,hue='Result'
    ,hue_order=[1,0]
    )
    )
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
my_hisplot(raw,17937,23,-20, 'M_T_ANT_power 2450MHz BY REF (sapphire) (F7Pro)_7.07%');
# %%
ppk_result(ppk_df(raw,17937,23), upper=5, lower=-2)
# %%
my_hisplot(raw,17936,12,-20, 'FT1_GPS_ (L1 + L5) by ref(Glass)_6.83%');
# %%
ppk_result(ppk_df(raw,17936,12), lower=-1.5, upper=1.5)
# %%
my_hisplot(raw.query("Item68 != 0"),17788,68,-20, 'HT_GPS_L5 by ref (7x PRO)_5.34%');
#%%
ppk_result(ppk_df(raw,17788,68), lower=-3, upper=1)
# %%
my_hisplot(raw,17787,60,-20, 'CT_GPS_ (L1 + L5) by ref_3.73%');
# %%
ppk_result(ppk_df(raw,17787,60), lower=-2, upper=2)
# %%
my_hisplot(raw.query("Item21 != 0"),17788,21,-20, 'HT_GPS_L5 by ref (7 PRO)_2.35%');
# %%
ppk_result(ppk_df(raw.query("Item21 != 0"),17788,21), lower=-2, upper=2)
# %%
