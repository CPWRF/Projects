# %%
import pandas as pd
from plotnine import *
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
#%%
# SO = pd.read_excel('MK3_PR_ASSY_SO.xlsx').JobNo
testresult = (pd.read_excel('FR165_FFP_PR_60.0_-41.17.xlsx', sheet_name='PR_45degree_0.51%_total72.15')
              .assign(ProcessType = lambda df: df.ProcessType.str.replace("FR165_",''))
              .astype({"ItemNameType":'int64',"Item":'int16'})
              .iloc[[1,2,3],:]
              )
testresult
# %%
ItemNameType = testresult['ItemNameType'].tolist()
item_name_type_str = ', '.join([f"'{i}'" for i in ItemNameType])
Item = testresult['Item'].tolist()
item_type_str = ','.join([f"Item{i},Item{i}St" for i in Item])
# %%
assy_query = f"""
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
16624108,16624109,16624110,16624111,16624112,16624113,16624114,16624115,16624116,16624117,16624118,16624119,16624120,16624121,16624122,16624123,16624124,
16624125,16624126,16624127,16624128,16624129,16624130,16624131,16624132,16624133,16624134,16624135,16624136,16624137,16624138,
16624139,16624140,16624141,16624142,16624143,16624144,16624145,16627471,16627472,16627473,16627474,16627475,16627476,16627477,16627478,16627479,
16627480,16627481,16627482,16627483,16627484,16627485,16627486,16627487,16627488,16627489,16627490,16627491,16627492,16627493,16627494,16627495,16627496,16627497,16627498,16627499,16627500,16627501,16627502,16627503,16627504,16627505,16627506,16627507,
16627508,16627509,16627510,16627511,16627512,16627513,16627514,16627515,16627516,16627517,16627518,16627519,16627520,16627521,16635681,16635682
)
"""
smt_query = f"""
SELECT
    ItemNameType,
    SO,
    f1.tDateTime,
    f1.Station,
    f1.StationID,
    failitem,
    Item136,
    Item136St,
    Item42,
    Item42St
FROM ate_db_tblcpu.dbo.TblCpu f1
JOIN [dbo].[TblCpu2] f2 on f1.tDateTime = f2.tDateTime and f1.tDateTime = f2.tDateTime
Where ItemNameType = 18734
and f1.SO in (
16624146,16624147,16624148,16624149,16624150,16624152,16624154,16628584,16628585,16629000,16629001
)
"""
connection_string_assy = "DRIVER={SQL Server};SERVER=XINWPD-ATESQLR;DATABASE=ate_db_tblfinal_new;UID=ate_oper;PWD=ate.oper"
connection_url_assy = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_assy})
engine_assy = create_engine(connection_url_assy)
assy = pd.read_sql(assy_query, engine_assy)

connection_string_smt = "DRIVER={SQL Server};SERVER=XINWPD-ATESQLR;DATABASE=ate_db_tblcpu;UID=ate_oper;PWD=ate.oper"
connection_url_smt = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_smt})
engine_smt = create_engine(connection_url_smt)
smt = pd.read_sql(smt_query, engine_smt)
# %%
def my_ggplot(df,itemnametype, item, lower, title):
    print(
        ggplot(assy
               .replace(-999,lower)
               .query(f"ItemNameType == {itemnametype} and Item{item}St.isin([0,1])")
               .astype({f"Item{item}St":"category"})
                )
        + aes(x=f'Item{item}', fill=f'Item{item}St')
        + geom_histogram(position='identity', alpha=0.5)
        + facet_wrap(["Station","StationID"])
        # + facet_grid("Station~StationID")
        + labs(title=title)
        + theme_538()
        + theme(dpi=300)
    )
my_ggplot(assy, 18825, 46, -10, 'test')
# my_ggplot(assy, 18828, 67, -10, 'test')
#%%
for i in range(len(testresult)):
    my_hisplot_SQL(assy,
                   testresult.ItemNameType.iloc[i], 
                   testresult.Item.iloc[i], 
                   -10,
                   f'{i+1}_{testresult.ProcessType.iloc[i]}_{testresult.ItemName.iloc[i]}_{testresult.Retest.iloc[i]}%')
# %%
my_hisplot_SQL(smt, 18734, 136, -10, 'AutoATE_PTC resistance')
# %%
my_hisplot_SQL(smt, 18734, 42, -10, 'AutoATE_Conducted GPS Sensitivity C/No L1')
# %%
(
    ggplot(smt
           .query("Item136St.isin([0,1])")
           .astype({"Item136St":'category'})
           .assign(Profile = smt.SO.where(~smt.SO.isin(['16624147','16624149']),'1_OM325')
                   .where(~smt.SO.isin(['16624148']),'2_OM325')
                   .where(~smt.SO.isin(['16628585']),'3_OM325*2x')
                   .where(~smt.SO.isin(['16629001','16624152']),'3_M705')
                   .where(smt.SO.isin(['16624147','16624148','16624149','16628585','16629001','16624152']),'3_OM325')
                   )
           )
    + aes(x='SO', y='Item136')
    + ggtitle('FR165_AutoATE_PTC resistance')
    + geom_violin(aes(color='Profile'))
    + geom_point(aes(fill = 'Item136St'))
    + geom_hline(yintercept=5, color='red', linetype='--')
    + geom_hline(yintercept=6, color='red', linetype='--')
    + theme(figure_size=(10, 6))
)
# %%
