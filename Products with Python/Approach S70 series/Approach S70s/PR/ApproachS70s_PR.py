# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
testresult = pd.read_excel('Approach S70s_45.xlsx',sheet_name='45')
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
    # .query("CountESN > CountESN.quantile(0.05)")
    .query("Retest >= Retest.mean()")
    # .Retest.mean().round(2)
    )
filter(testresult)
# %%
filter(testresult).to_excel('Triggerby45.xlsx', index=False)
# %%
raw = pd.read_excel('ASSYRAW.xlsx')
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
my_hisplot(raw,16521,57,-20, 'FT1_GPS L1 Radiated Sensitivity (S70s)_9.09%');
# %%
ppk_result(ppk_df(raw,16521,57), lower=-2, upper=3.2)
# %%
my_hisplot(raw,16521,45,-20, 'FT1_GPS L1 Radiated Sens BL=80% (S70s)_3.13%');
# %%
ppk_result(ppk_df(raw,16521,45), lower=-5, upper=0)
# %%
my_hisplot(raw,16516,47,-20, 'CT_GPS L1 Radiated Sensitivity (S70s)_2.73%');
#%%
ppk_result(ppk_df(raw,16516,47), lower=-2.5, upper=5)
# %%
my_hisplot(raw,16518,46,-20, 'RT1_GPS L1 Radiated Sens BL=80% (S70s)_2.5%');
# %%
ppk_result(ppk_df(raw,16518,46), lower=-5, upper=1.5)