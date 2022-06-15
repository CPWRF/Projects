# %%
import pyodbc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.tseries.offsets import BDay
from datetime import datetime
import pytz
import os


# %%
scope = '2021-01'

# %%
my_query = """ 
SELECT [projectSizeId]
      ,[PROJECT_SIZE_NAME] as 'Project_Name'
      ,[typeName] as 'Phase'
      ,[status]
      ,[rejectReason]
      ,[kickOffMeetingDate]
      ,[baseOverDueDate] as 'closeMeetingDate'
      ,[submitDate] as 'GMLASubmitDate'
      ,[IsByPass] 
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST_CONFIRM]

  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on projectSizeId = PROJECT_SIZE_ID
  /* Join project names */

  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE]
  ON typeId = [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE].id
  /* Join GMLA#1/#2/#3 name*/

  WHERE [IsByPass] = '0'
"""


# %%
server = 'T1-PE-SUPPORT' 
database = 'PR_WEB2' 
username = 'pieng' 
password = 'Q2iT5cwHJW3FH' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
query = my_query
df = pd.read_sql(query, cnxn)


# %%
df.replace('0001-01-08 00:00:00.0000000 +08:00', np.nan, inplace=True)

# %%
df.closeMeetingDate = pd.to_datetime(df.closeMeetingDate, utc=True)
df.GMLASubmitDate = pd.to_datetime(df.GMLASubmitDate,utc=True)

# %%
df.closeMeetingDate = df.closeMeetingDate.dt.tz_convert('Asia/Taipei')
df.GMLASubmitDate = df.GMLASubmitDate.dt.tz_convert('Asia/Taipei')

# %%
df['target_GMLASubmitDate'] = (df.closeMeetingDate + BDay(9))

# %%
"""
Forecast
"""

# %%
forecast = df[(df.status == 0) & (df.target_GMLASubmitDate> datetime.now(pytz.timezone('Asia/Taipei')))].sort_values('closeMeetingDate')
forecast

# %%
df.dropna(axis=0, subset=['GMLASubmitDate'], inplace=True)

# %%
df['on_time'] = df.target_GMLASubmitDate.dt.strftime('%Y-%m-%d') >= df.GMLASubmitDate.dt.strftime('%Y-%m-%d')

# %%
on_time = df.drop_duplicates(subset=['Project_Name','Phase']).sort_values(['Project_Name','Phase'])

# %%
"""
Handle delay_but_rejected projects
"""

# %%
def delay_but_rejected(on_time, rejectReason):
    if on_time == False and rejectReason != None:
        return True
    else:
        return False

# %%
on_time['delay_but_rejected'] = np.vectorize(delay_but_rejected)(on_time['on_time'], on_time['rejectReason'])

# %%
on_time = on_time[on_time.target_GMLASubmitDate> scope]

# %%
"""
Delayed projects
"""

# %%
delayed_projects = on_time[(on_time.on_time == False)].sort_values('target_GMLASubmitDate')
delayed_projects

# %%
actual_delayed_projects = on_time[(on_time.on_time == False) & (on_time.delay_but_rejected == False)].sort_values('target_GMLASubmitDate')
actual_delayed_projects

# %%
"""
Resample
"""

# %%
on_time_resampled = on_time.set_index('target_GMLASubmitDate').resample(rule='BM').agg({'Project_Name':'count','on_time':'sum','delay_but_rejected':'sum'})

# %%
on_time_resampled.rename(columns={'Project_Name':'total_projects','on_time':'on_time_projects','rejectReason':'rejcted_projects'}, inplace=True)

# %%
"""
Convert datetime format
"""

# %%
on_time_resampled.reset_index(inplace=True)

# %%
on_time_resampled['target_GMLASubmitDate'] = on_time_resampled['target_GMLASubmitDate'].dt.strftime('%Y-%m')

# %%
on_time_resampled = on_time_resampled.set_index('target_GMLASubmitDate')

# %%
on_time_resampled['on_time_rate'] = (100* (on_time_resampled.on_time_projects / on_time_resampled.total_projects)).round(2)

# %%
on_time_resampled['actual_on_time_rate'] = (100* ((on_time_resampled.on_time_projects+ on_time_resampled.delay_but_rejected) / on_time_resampled.total_projects)).round(2)

# %%
on_time_resampled



# %%
plt.figure(figsize=(20,7))
plt.grid()
sns.lineplot(data=on_time_resampled.on_time_rate, estimator=None, linewidth=3, alpha=0.5)
sns.lineplot(data=on_time_resampled.actual_on_time_rate, estimator=None, linewidth=3, alpha=0.8)
plt.legend(['on_time_rate','actual_on_time_rate'], loc='lower right')
plt.savefig(os.getcwd()+'\on_time_tread')

# %%
