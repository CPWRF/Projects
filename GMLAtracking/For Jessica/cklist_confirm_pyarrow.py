# %%
import pyodbc
from numpy import vectorize
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import BDay
from datetime import datetime
from os import getcwd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
# from UliPlot.XLSX import auto_adjust_xlsx_column_width
#%%
# SQL
# Get GMLA list
cklist_confirm_query = """ 
SELECT [projectSizeId]
      ,[PROJECT_SIZE_NAME] as 'Project_Name'
      ,[PROJECT_CATEGORY] as 'Segment'
      ,LEFT([typeName],4) + Right([typeName],1) as 'Phase'
      ,[status]
      ,[rejectReason]
      /*,[kickOffMeetingDate]*/
      ,[baseOverDueDate] as 'actCloseMeeting'
      ,[submitDate] as 'actGMLASubmit'
      /*,[IsByPass]*/
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST_CONFIRM]

  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on projectSizeId = PROJECT_SIZE_ID
  /* Join project names and segment */

  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE]
  ON typeId = [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE].id
  /* Join GMLA#1/#2/#3 name*/

  WHERE [IsByPass] = '0'
"""
# Get design review date which sync PM system
project_schedule_query = """ 
SELECT [ProjectSizeId] as 'projectSizeId'
      /*
      ,[PROJECT_NAME]
      ,[T_GT_ProjectSchedule].[TASK_ID]
      */
      ,[DESC_OF_TASK]
      /*
      ,[T_GT_TaskBaseInfo].[Note]
      ,[IsPM]
      */
      ,DATEADD(DAY,-21,[Current_Date]) as 'estCloseMeeting'
      /* Design review -21 days */
  FROM [PR_WEB2].[dbo].[T_GT_ProjectSchedule]

  LEFT JOIN [PR_WEB2].[dbo].[T_GT_TaskBaseInfo] 
  ON [T_GT_ProjectSchedule].[TASK_ID] = [T_GT_TaskBaseInfo].TASK_ID

  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on ProjectSizeId = [T_PS_ProdSizeRelateInfo].PROJECT_SIZE_ID
  
  WHERE DESC_OF_TASK
  IN ('Mechanical Design Review','Factory Prototype Design Review','Pilot Run Design Review')
"""
# Get Project Risk
cklist_issue_query = """
SELECT [T_GMLA_CKLIST_ISSUE].[projectSizeId]
      /*,[PROJECT_CATEGORY] as 'Segment'*/
      ,[PROJECT_SIZE_NAME] as 'Project_Name'
      ,LEFT([typeName],4) + Right([typeName],1) as 'Phase'
      /*,[T_GMLA_CKLIST_ISSUE].[categoryId]*/
      ,[riskType] as 'Risk'
      /*,[categoryName] as 'Category'*/
      /*,[T_GMLA_CKLIST_ISSUE].[id]*/
      /*,[no] as 'No'*/
      /*,[T_GMLA_CKLIST_ISSUE].[status]*/
      /*,[T_GMLA_CKLIST_ISSUE].[updated_at]*/
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST_ISSUE]
  
  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on projectSizeId = PROJECT_SIZE_ID
  /* Join project names */
  
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE]
  ON typeId = [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE].id
  /* Join GMLA#1/#2/#3 name*/
  
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_CATEGORY]
  ON [T_GMLA_CKLIST_ISSUE].categoryId=[T_GMLA_BS_CATEGORY].id
  /* Join 6 category name via id */

  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_CKLIST]
  ON ([T_GMLA_CKLIST_ISSUE].[categoryId] = [T_GMLA_CKLIST].[categoryId]
  AND [T_GMLA_CKLIST_ISSUE].id = [T_GMLA_CKLIST].id
  AND [T_GMLA_CKLIST_ISSUE].projectSizeId = [T_GMLA_CKLIST].projectSizeId
  AND [T_GMLA_CKLIST_ISSUE].typeId = [T_GMLA_CKLIST].typeId)
  /* Join serval datas */
"""
# Get GMLA score
gmla_cklist_query = """
SELECT [projectSizeId]
      ,LEFT([typeName],4) + Right([typeName],1) as 'Phase'
      /*,[categoryId]
      ,[no]*/
      ,[result]
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST]
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE]
  ON [T_GMLA_CKLIST].typeId = [T_GMLA_BS_VERSION_TYPE].id
"""

connection_string = "DRIVER={SQL Server};SERVER=T1-PE-SUPPORT;DATABASE=PR_WEB2;UID=pimes2;PWD=LhZEv9JtGsZNX"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

cklist_confirm = pd.read_sql(cklist_confirm_query, engine, dtype_backend='pyarrow')
project_schedule = pd.read_sql(project_schedule_query, engine, parse_dates='estCloseMeeting', dtype_backend='pyarrow')
cklist_issue = pd.read_sql(cklist_issue_query, engine, dtype_backend='pyarrow')
gmla_cklist = pd.read_sql(gmla_cklist_query, engine, dtype_backend='pyarrow')
#%%
# Hanlde cklist_issue for project risk info.
# Risk 4 = blue 1 star = Risk 2, replace blue star
def tweak_cklist_issue(df):
    return(df
    .assign(Risk = df.Risk.replace(to_replace= 4,value = 2))
    .astype({"projectSizeId":'int16[pyarrow]',"Phase":"category","Risk":"category"})
    .sort_values('Risk')
    .drop_duplicates(subset=['projectSizeId','Project_Name','Phase'], keep='first')
    .sort_values('projectSizeId')
    )
def tweak_cklist_confirm(df):
    return(df
        .assign(actCloseMeeting = df.actCloseMeeting.replace('0001-01-08 00:00:00.0000000 +08:00',None))
        .assign(actCloseMeeting = lambda df_ : (pd.to_datetime(df_.actCloseMeeting, utc=True).dt.tz_convert('Asia/Taipei')),
                actGMLASubmit = lambda df_ : (pd.to_datetime(df_.actGMLASubmit, utc=True).dt.tz_convert('Asia/Taipei')),
                rejectReason = lambda df_ : df_.rejectReason.notnull())
        .astype({"projectSizeId":'int16[pyarrow]',"Phase":"category","status":"boolean","Segment":"category"})
        .query('projectSizeId != 1124') #Project id 1124 is aborted
    )
def tweak_project_schedule(df):
    return(df
    .assign(estCloseMeeting = df.estCloseMeeting.dt.tz_convert('Asia/Taipei')
            ,Phase = df.DESC_OF_TASK.map({'Mechanical Design Review':'GMLA1','Factory Prototype Design Review':'GMLA2','Pilot Run Design Review':'GMLA3'}))
    .astype({"projectSizeId":'int16[pyarrow]',"DESC_OF_TASK":"category","Phase":'category'})
    .drop_duplicates(subset=['projectSizeId','Phase']) # Some project have multi-design review date in PMsystem
    .drop('DESC_OF_TASK', axis=1)
    )
#%%
# Merge project_schedule
overall = pd.merge(left=tweak_cklist_confirm(cklist_confirm), 
                   right=tweak_project_schedule(project_schedule), 
                   how='left', on=['projectSizeId','Phase'])
#%%
def targetGMLASubmit(actCloseMeeting, estCloseMeeting):
    if actCloseMeeting is pd.NaT:
        return (estCloseMeeting + BDay(8))
    else:
        return (actCloseMeeting + BDay(8))
def on_time(actualDate, targetDate):
    if actualDate is pd.NaT or targetDate is pd.NaT:
        return pd.NaT
    elif actualDate > targetDate:
        return 0
    else:
        return 1
def tweak_overall(df):
    return(df
    .assign(targetGMLASubmit = vectorize(targetGMLASubmit)(df.actCloseMeeting, df.estCloseMeeting))
    .drop(columns=['actCloseMeeting','estCloseMeeting'])
    .assign(actGMLASubmit = lambda df_ : df_.actGMLASubmit.dt.date
            ,targetGMLASubmit = lambda df_ : df_.targetGMLASubmit.dt.date
            ,on_time = lambda df_: vectorize(on_time)(df_.actGMLASubmit, df_.targetGMLASubmit))
    .astype({'on_time':'bool'})
    )
#%%
# Merge cklist_issue to get "Risk"
overall2 = pd.merge(left=tweak_overall(overall), right=tweak_cklist_issue(cklist_issue), 
                   on=['projectSizeId','Project_Name','Phase'], how='left')
#%%
# def color_risk(status, risk):
#     if status == 1:
#         if risk == 3:
#             return 'Red'
#         elif risk == 2:
#             return "Yellow"
#         else:
#             return "Green"
#     else:
#         return pd.NA
def tweak_overall2(df):
    return(df
    .assign(Risk = df.Risk.map({3:'Red',2:"Yellow",1:"Green",0:'Green'}).astype('category')
            ,delay_but_rejected = (df.rejectReason == True) & (df.on_time == False))
    )
def tweak_gmla_cklist(df):    
    return(df
    .assign(result = df.result.map({3:1, 1:0, 2:0}))
    # Result 3 = complete, 1 = incomplete, 2 = yellow light, 0 = GMLA is open
    .groupby(['projectSizeId','Phase']).agg({'Phase':'count','result':'sum'})
    .rename(columns={'Phase':'totalProject'})
    .assign(Score = lambda df_ : 100*(df_.result / df_.totalProject).round(4))
    .reset_index()
    [['projectSizeId','Phase','Score']]
    .astype({"projectSizeId":'int16[pyarrow]',"Phase":"category","Score":"float16"})
    )
#%%
# Get GMLA score and merge to overall
overall3 = pd.merge(left=tweak_overall2(overall2), right=tweak_gmla_cklist(gmla_cklist), on=['projectSizeId','Phase'], how='left')
#%%
def complete_rate(df):
    return(df
    .query("actGMLASubmit.notnull()")
    .assign(targetGMLASubmit = pd.to_datetime(df['targetGMLASubmit']))
    .set_index('targetGMLASubmit')
    .resample(rule='BM')
    .agg({'Project_Name':'count','status':'sum'})
    .assign(complete_rate= lambda df_ : 100*(df_.status / df_.Project_Name))
    )
def on_time_rate(df):
    return(df
    .query("status==1")
    .assign(targetGMLASubmit = pd.to_datetime(df['targetGMLASubmit']))
    .set_index('targetGMLASubmit')
    .resample(rule='BM')
    .agg({'Project_Name':'count','on_time':'sum','delay_but_rejected':'sum'})
    .rename(columns={'Project_Name':'total_projects','on_time':'on_time_projects','rejectReason':'rejcted_projects'})
    .loc[datetime.now()-pd.DateOffset(years=1):datetime.now()]
    .assign(actual_on_time_rate = lambda df_ : (100* ((df_.on_time_projects+ df_.delay_but_rejected) / df_.total_projects)))
    )
#%%
# Draw one year data
ax = on_time_rate(overall3)[datetime.now()-pd.DateOffset(years=1):datetime.now()+pd.DateOffset(months=1)].actual_on_time_rate.plot(figsize=(18,6), marker='o', markersize=10 ,lw=3, grid=True, alpha=0.5, label = 'On-time rate')
ax2 = complete_rate(overall3)[datetime.now()-pd.DateOffset(years=1):datetime.now()+pd.DateOffset(months=1)].complete_rate.plot(figsize=(18,6), marker='o', markersize=10 ,lw=3, grid=True, alpha=0.5, label = 'Complete rate')
ax.set_xlabel('Time');
ax.set_ylabel('Complete rate');
ax.set_title('Monthly GMLA Complete & On-time Rate Overview - within a year ~');
plt.legend()
plt.savefig(getcwd()+'\Complete and on_time rate',bbox_inches = "tight", facecolor='white', transparent=False, dpi=300)
#%%
def overall_show(df):
    return(df
    [['projectSizeId','Segment','Project_Name','Phase','Risk','Score','status','targetGMLASubmit','actGMLASubmit','on_time','delay_but_rejected']]
    # .set_index('projectSizeId')
    # .sort_index()
    .sort_values(['projectSizeId','Phase'], ascending=False)
    .assign(status = lambda df_ : df_.status.map({True:'Complete',False:'Incomplete'})
            ,on_time = lambda df_ : df_.on_time.map({True:'Y',False:'N'}))
    )
#%%
# Excel writer
with pd.ExcelWriter(getcwd()+'\data.xlsx', engine='openpyxl') as writer:
    overall_show(overall3).to_excel(writer, sheet_name='overall', index=False)
    # auto_adjust_xlsx_column_width(overall_show(overall3), writer, sheet_name="overall", margin=5)
    
    complete_rate(overall3).to_excel(writer, sheet_name='complete_rate', index=False)
    # auto_adjust_xlsx_column_width(complete_rate(overall3), writer, sheet_name="complete_rate", margin=5)
    
    on_time_rate(overall3).to_excel(writer, sheet_name='on_time_rate', index=False)
    # auto_adjust_xlsx_column_width(on_time_rate(overall3), writer, sheet_name="on_time_rate", margin=5)