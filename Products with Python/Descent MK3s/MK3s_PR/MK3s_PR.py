# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
plt.style.use('fivethirtyeight')
#%%
# SO = pd.read_excel('MK3_PR_ASSY_SO.xlsx').JobNo
testresult = (pd.read_excel('MK3s_FFP_PR_79.0_64.98.xlsx', sheet_name='PR_45degree_1.06%_total122.63')
              .assign(ProcessType = lambda df: df.ProcessType.str.replace("DescentMK3_",''))
              .query("ItemName.str.contains('GPS', case=False)| ItemName.str.contains('TX') | ItemName.str.contains('ANT')")
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
    SO,
    f1.tDateTime,
    f1.Station,
    f1.StationID,
    failitem,
    {item_type_str}
FROM ate_db_tblfinal_new.dbo.TblFinal f1
JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime and f1.tDateTime = f2.tDateTime
Where ItemNameType in ({item_name_type_str})
and f1.SO in (
16603157,16603158,16603160,16603162,16603164,16603166,16603167,16603168,16603169,16603171,16603172,16603173,16603174,
16603176,16603177,16603178,16603179,16603181,16603183,16603185,16603187,16603189,16603190,16603191,16603192,16603193,16603194,16603196,16603198,16603200,16603202,16603204,16603206,
16603207,16603208,16603209,16603210,16603211,16603213,16603215,16603217,16603219,16603221,16603222,16603223,16603224,16603225,16603226,16603862,16612077,16612078,16612079,16650189
)
and f1.tDateTime > '2023-09-25'
"""
connection_string = "DRIVER={SQL Server};SERVER=SHIWPD-ATESQLR;DATABASE=ate_db_tblfinal_new;UID=ate_oper;PWD=ate.oper"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
raw = (pd.read_sql(raw_query, engine)
       .assign(Item199 = lambda df : df.Item199.clip(upper=10)) #Clip Item199
       )
# %%
def my_hisplot_SQL(df,itemnametype, item, lower, title):
    plt.figure(dpi=130)
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