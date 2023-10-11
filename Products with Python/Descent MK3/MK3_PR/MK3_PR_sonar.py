# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
plt.style.use('bmh')
# %%
raw_query = f"""
SELECT
    ItemNameType,
    f1.tDateTime,
    f1.Station,
    f1.StationID,
    failitem,
    SerialNumber,
    Item39,
    Item39St
FROM ate_db_tblfinal_new.dbo.TblFinal f1
Where ItemNameType = 18213
and f1.tDateTime > '2023-10-01'
"""
connection_string = "DRIVER={SQL Server};SERVER=SHIWPD-ATESQLR;DATABASE=ate_db_tblfinal_new;UID=ate_oper;PWD=ate.oper"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
raw = pd.read_sql(raw_query, engine)
raw
# %%
plt.figure(dpi=400)
(raw
.sort_values(['SerialNumber','tDateTime'])
.drop_duplicates('SerialNumber', keep='last')
.assign(tDateTime = raw.tDateTime.dt.tz_localize('UTC').dt.tz_convert('Asia/Taipei'))
.query("tDateTime.dt.day == 2")
.query("Item39St == 1")
.set_index('tDateTime')
.resample('60Min')
[['Item39']]
.median()
).plot(title='MK3_Sonar TX 40K - 0 degree RMS (Moving Avg.=1hr)',legend=None, color='k');
plt.axhline(y=0.3, color='red', ls='--')
plt.text(x = "2023-10-02 9:10", y=0.20, s='LSL', color='red')
plt.fill_between(x=["2023-10-02 10:00","2023-10-02 12:00"], y1=[2], color='red', alpha=0.3)
plt.text(x = "2023-10-02 10:20", y=0.75, s='Trend down', color='red')

plt.fill_between(x=["2023-10-02 12:00","2023-10-02 13:00"], y1=[2], color='green', alpha=0.3)
plt.text(x = "2023-10-02 12:10", y=0.75, s='Adjust', color='green')

plt.fill_between(x=["2023-10-02 17:00","2023-10-02 18:00"], y1=[2], color='red', alpha=0.3)
plt.text(x = "2023-10-02 17:00", y=0.75, s='Trend down', color='red')
plt.ylim([0,2])
plt.savefig("High resoltion.png",dpi=300)