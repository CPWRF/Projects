# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
plt.style.use('fivethirtyeight')
#%%
# SO = pd.read_excel('MK3_PR_ASSY_SO.xlsx').JobNo
testresult = (pd.read_excel('MK3_FFP_PR_84.0_-14.08.xlsx', sheet_name='PR_45degree_1.31%_total170.52')
              .assign(ProcessType = lambda df: df.ProcessType.str.replace("DescentMK3_",''))
              .query("ItemName.str.contains('ref', case=False)| ItemName.str.contains('RMS Average')")
              .astype({"ItemNameType":'int64',"Item":'int16'})
              )
testresult
# %%
ItemNameType = testresult['ItemNameType'].tolist()
item_name_type_str = ', '.join([f"'{i}'" for i in ItemNameType])
Item = testresult['Item'].tolist()
item_type_str = ','.join([f"Item{i},Item{i}St" for i in Item])
# %%
raw_query = f"""
SELECT
    ItemNameType,
    f1.tDateTime,
    f1.Station,
    f1.StationID,
    failitem,
    {item_type_str}
FROM ate_db_tblfinal_new.dbo.TblFinal f1
JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime
Where ItemNameType in ({item_name_type_str})
and f1.tDateTime > '2023-09-05'
"""
connection_string = "DRIVER={SQL Server};SERVER=SHIWPD-ATESQLR;DATABASE=ate_db_tblfinal_new;UID=ate_oper;PWD=ate.oper"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
raw = pd.read_sql(raw_query, engine)
raw.sample()
# %%
def my_hisplot_SQL(df,itemnametype, item, lower, title):
    plt.figure(dpi=100)
    plt.title(title)
    sns.histplot(data = (df
                         .replace(-999,lower)
                         .query(f"ItemNameType == {itemnametype} and Item{item}St.isin([0,1])")
                        )
    ,x=f'Item{item}'
    ,hue=f'Item{item}St'
    ,hue_order=[1,0]
    ,palette='Set2'
    )
#%%
for i in range(len(testresult)):
    my_hisplot_SQL(raw,
                   testresult.ItemNameType.iloc[i], 
                   testresult.Item.iloc[i], 
                   -10,
                   f'{i+1}_{testresult.ProcessType.iloc[i]}_{testresult.ItemName.iloc[i]}_{testresult.Retest.iloc[i]}%')