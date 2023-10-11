# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
plt.style.use('fivethirtyeight')
# %%
raw_query = f"""
SELECT
    ItemNameType,
    f1.tDateTime,
    f1.SerialNumber,
    f1.Station,
    f1.StationID,
    failitem,
    Item42,
    Item42St
FROM ate_db_tblfinal_new.dbo.TblFinal f1
JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime
Where ItemNameType in (18191)
and f1.tDateTime > '2023-09-05'
"""
connection_string = "DRIVER={SQL Server};SERVER=SHIWPD-ATESQLR;DATABASE=ate_db_tblfinal_new;UID=ate_oper;PWD=ate.oper"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
raw = pd.read_sql(raw_query, engine)
raw
# %%
sns.stripplot(data=(raw
              .query("Item42St.isin([0,1])")
              .sort_values('tDateTime')
              .drop_duplicates('SerialNumber',keep='last')
              ), 
              x='StationID', y='Item42',
              hue='Item42St',
              hue_order=[1,0]
              )
# %%
plt.figure(dpi=150)
sns.stripplot(data=(raw
            # .query("Item42St.isin([0,1])")
            .query("SerialNumber.isin(['3457337472','3457337517','3457337355'])")
            .drop_duplicates()
            # .assign(ESN = raw.SerialNumber.where(raw.SerialNumber.isin(['3457337422','3457337517','3457337355']),'Others'))
              ), 
              x='StationID', y='Item42',
              hue='SerialNumber'
              )
sns.violinplot(data=(raw
            .query("Item42St.isin([0,1,5])")
            .drop_duplicates()
            ),
            x='StationID', y='Item42',color='gray', alpha=0.3, inner=None)
plt.legend(loc="lower left")
# %%
sns.swarmplot(data=(raw
              # .query("Item42St.isin([0,1])")
              .assign(ESN = raw.SerialNumber.where(raw.SerialNumber.isin(['3457337472','3457337517','3457337355']),'Others'))
              .drop_duplicates()
              ), 
              x='StationID', y='Item42',
              hue='ESN'
              # hue_order=[1,0]
              )