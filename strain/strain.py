import pyodbc
import pandas as pd
from os import getcwd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from UliPlot.XLSX import auto_adjust_xlsx_column_width

gpn = input ("Enter whole 105-GPN (according to SMTVip) :")

strain_query = '''
SELECT  [StrainGauge].[gid]
      ,[gpn]
      ,[ver] as 'PCBver'
      ,[station]
      ,[Position]
      ,[TestRecord].[judge]
      ,[TestRecord].[stress] as 'Strain'
      ,[TestRecord].[WQ211] as 'Spec'
      ,[memo]
      ,[org]
      ,[createdata]
  FROM [SMTvip].[dbo].[StrainGauge]

  Left JOIN [SMTvip].[dbo].[TestRecord] 
  on [StrainGauge].[gid] = [TestRecord].[gid]
  where gpn = '{}'
  ORDER by profdate DESC
'''.format(gpn)

connection_string = "DRIVER={SQL Server};SERVER=T1-PE-SUPPORT;DATABASE=PR_WEB2;UID=pimes2;PWD=LhZEv9JtGsZNX"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
raw = pd.read_sql(strain_query, engine)

def pivot_raw(raw):
    return(raw
    .assign(judge = raw.judge.map({'OK':1, 'NG':0}).astype('int8'))
    .sort_values('createdata', ascending=False)
    .drop_duplicates(subset=['PCBver','station','Position','memo', 'judge']) #The reason subset consider 'judge' is same position may have 2 strain gauge and each of gauge may have different result
    .groupby(['station','memo','PCBver','createdata','Position'])
    ['judge']
    .min() #If one of results in the same position is 0, take 0 as output.
    .unstack('Position')
    .sort_index(level=['station','createdata'],ascending=False)
    .style.applymap(lambda val : "background-color: red" if val == 0 else "")
    )

with pd.ExcelWriter(getcwd()+'\{}_StrainResult.xlsx'.format(gpn), engine='openpyxl') as writer:
    pivot_raw(raw).to_excel(writer, sheet_name='pivot')
    raw.to_excel(writer, sheet_name='raw', index=False)