# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import manufacturing as mn
# %%
testresult = pd.read_excel('Approach S70_PR_ASSY_WW.xlsx',sheet_name='45')
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
# filter(testresult).to_excel('Triggerby45.xlsx', index=False)
# %%
raw = pd.read_excel('ASSYRAW.xlsx')
# %%
def tweak_df(df,itemnametype, item, lower):    
    return(df
    .query(f"ItemNameType=={itemnametype} and failitem.isin([0,{item}]) and Item{item}>{lower}")
    [['Result',f'Item{item}']])
def my_hisplot(df,itemnametype, item, lower, title):
    print(f"{ppk_df(df,itemnametype, item).agg(['min','max'])}")
    plt.figure(dpi=100)
    plt.title(title)
    return(sns.histplot(data = (tweak_df(df,itemnametype, item, lower))
    ,x=f'Item{item}'
    ,hue='Result'
    ,hue_order=[1,0]))
def ppk_df(df,itemnametype, item):
    return(df
    .query(f"ItemNameType=={itemnametype} and Result==True")
    [f'Item{item}'])
def ppk_result(df, upper, lower):
    pp = mn.calc_pp(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    ppk = mn.calc_ppk(df, upper_specification_limit=upper, lower_specification_limit=lower).round(2)
    sugg = mn.suggest_specification_limits(df)
    print(f"ppk={ppk}, pp={pp}, sugg={sugg}")
# %%
plt.style.use('fivethirtyeight')
# %%
my_hisplot(raw.query("Item70 != 0"),16516,70,-20, 'CT_GPS L1 Radiated Sensitivity (S70)_21.49%');
ppk_result(ppk_df(raw,16516,70), lower=-3, upper=1)
# %%
my_hisplot(raw.query("Item50 != 0"),16517,50,-20, 'HT_GPS L1 Radiated Sensitivity (S70)_12.28%');
ppk_result(ppk_df(raw,16517,50), lower=-3, upper=1)
# %%
my_hisplot(raw.query("Item63 != 0"),16516,63,-20, 'CT_GPS L5 Radiated Sensitivity (S70)_8.77%');
ppk_result(ppk_df(raw,16516,63), lower=-3, upper=2)
# %%
my_hisplot(raw,16518,115,-20, 'RT1_GPS L5 Radiated Sensitivity (S70)_4.95%');
ppk_result(ppk_df(raw,16518,115), lower=-3, upper=3)
# %%
my_hisplot(raw,16521,89,-20, 'FT1_GPS L1 Radiated Sensitivity (S70)');
ppk_result(ppk_df(raw,16521,89), lower=-5, upper=2)
# %%
my_hisplot(raw,16521,78,-20, 'FT1_GPS L5 Radiated Sensitivity BL=80% (S70)');
ppk_result(ppk_df(raw,16521,78), lower=-4, upper=0.5)