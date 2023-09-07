# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import manufacturing as mn
# %%
raw = pd.read_excel('FP165_FFP.xlsx')
# %%
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
# plt.style.use('fivethirtyeight')
def my_hisplot_SQL(df,itemnametype, item, lower, higher, title):
    # print(f"{ppk_df(df,itemnametype, item).agg(['min','max'])}")
    plt.figure(dpi=100)
    plt.title(title)
    sns.histplot(data = (raw
                         .replace(-999,lower)
                         .query(f"ItemNameType == {itemnametype} & Item{item}St.isin([0,1,2]) & Item{item} < {higher}")
                        )
    ,x=f'Item{item}'
    ,hue=f'Item{item}St'
    ,hue_order=[1,0,2]
    ,palette='Set2'
    )
# %%
item = [74,42,34,190,71,9,190]
# itemnametype = [18191,18191,18192,18192,18195,18195,18200,18200,18213,18213,18213]
testresult = (pd.read_excel('FR165_FFP_0.51_51.11.xlsx', sheet_name='FFP_45degree0.51%_total51.11')
              .query('Item.isin(@item) & ItemNameType != 18735')
              .sort_values("Retest", ascending=False)
              )
testresult
#%%
for i in range(len(testresult.index)):
    my_hisplot_SQL(raw, 
                   testresult.ItemNameType.iloc[i], 
                   testresult.Item.iloc[i], 
                   lower=-10,
                   higher=9999999,
                   title=f'{i+1}_{testresult.ProcessType.iloc[i]}_{testresult.ItemName.iloc[i]}_{testresult.Retest.iloc[i]}%')