# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import manufacturing as mn
# %%
# testresult = pd.read_excel('MARQ_carbon_PR.xlsx',sheet_name='Test Result')
# # %%
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
#     # .query("CountESN > CountESN.quantile(0.07)")
#     .query("Retest >= Retest.mean()"))
# def degree(df):
#     return(tweak(df)
#     .Retest.mean().round(2))
# filter(testresult)
# %%
# filter(testresult).to_excel(f'Triggerby{degree(testresult)}percent.xlsx', index=False)
# %%
raw = pd.read_excel('MK3_FFP_raw.xlsx')
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
# def ppk_df(df,itemnametype, item):
#     return(df
#     .query(f"ItemNameType=={itemnametype} and Item{item}St==1")
#     [f'Item{item}']
#     )
# def ppk_result(df, upper, lower):
#     pp = mn.calc_pp(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
#     ppk = mn.calc_ppk(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
#     sugg = mn.suggest_specification_limits(df)
#     print(f"ppk={ppk}, pp={pp}, sugg={sugg}")
    
def my_hisplot_SQL(df,itemnametype, item, lower,title):
    # print(f"{ppk_df(df,itemnametype, item).agg(['min','max'])}")
    plt.figure(dpi=100)
    plt.title(title)
    sns.histplot(data = raw.query(
        f"ItemNameType == {itemnametype} and Item{item}St.isin([0,1]) and Item{item}>{lower}")
    ,x=f'Item{item}'
    ,hue=f'Item{item}St'
    ,hue_order=[1,0])
# %%
FT1 = 18195
FT2 = 18203
HT = 18192
CT = 18191
# %%
my_hisplot_SQL(raw, FT1, 150, -30, "FT1_Glonass_65 by ref")
# %%
my_hisplot_SQL(raw, FT2, 28, -30,"FT2_ANT Radiated TX Power")
# %%
my_hisplot_SQL(raw, FT1, 30, -30, "FT1_GPS_ (L1 + L5) by ref")
# %%
my_hisplot_SQL(raw, HT, 89, -30, "HT_GPS_L5 by ref")
# %%
my_hisplot_SQL(raw, CT, 60, -30, "CT_GPS_ (L1 + L5) by ref")
# %%
plt.title("FT1_Glonass_65 by ref")
sns.swarmplot(data=raw.query("ItemNameType==@FT1 & ~Item150St.isin([2,5])")
               , x='Station', y='Item150'
               , hue='StationID')