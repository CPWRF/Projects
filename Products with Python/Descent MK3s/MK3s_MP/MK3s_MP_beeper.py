# %%
import pandas as pd
from plotnine import ggplot, aes, geom_histogram, facet_wrap, labs, theme, theme_538, xlim, theme_bw
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
# %%
assy_query = f"""
SELECT
    ItemNameType,
    SO,
    f1.SerialNumber,
    f1.tDateTime,
    f1.Station,
    f1.StationID,
    failitem,
    Item212,
    Item212St,
    Item213,
    Item213St
FROM ate_db_tblfinal_new.dbo.TblFinal f1
JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime and f1.tDateTime = f2.tDateTime
Where ItemNameType = '17522'
/* and f1.SerialNumber = '3462815644' */
and f1.So = '16820075'
"""
connection_string_assy = "DRIVER={SQL Server};SERVER=SHIWPD-ATESQLR;DATABASE=ate_db_tblfinal_new;UID=ate_oper;PWD=ate.oper"
connection_url_assy = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_assy})
engine_assy = create_engine(connection_url_assy)
assy = pd.read_sql(assy_query, engine_assy)
# %%
def my_ggplot(df,itemnametype, item, lower, title):
    print(
        ggplot(assy
               .replace(-999,lower)
               .query(f"ItemNameType == {itemnametype} and Item{item}St.isin([0,1])")
               .dropna()
               .astype({f"Item{item}St":"category"})
                )
        + aes(x=f'Item{item}', fill=f'Item{item}St')
        + geom_histogram(position='identity', alpha=0.5)
        + facet_wrap(["Station","StationID"])
        # + facet_grid("Station~StationID")
        + labs(title=title, caption='-DPQE', subtitle='ShopOrder 16820075')
        + theme_bw()
        + theme(dpi=300)
        + xlim(40, 80)
    )
my_ggplot(assy, 17522, 212, -10, 'MK3s_Beeper Loudness')
# %%
(assy
 .query("Item212St.isin([0,1])")
 .groupby(['Station','StationID'])
 .agg(count = ('Item212St','count'), sum=('Item212St','sum'))
 .assign(yieldRate = lambda df: (100*df['sum']/df['count']).round(2))
 )