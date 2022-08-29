import pyodbc
import pandas as pd
from os import getcwd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from UliPlot.XLSX import auto_adjust_xlsx_column_width

gpn = input ("Enter whole 105-GPN :")

strain_query = '''
SELECT  [StrainGauge].[gid]
      ,[gpn]
      ,[ver] as 'PCB ver'
      ,[station]
      ,[Position]
      ,[TestRecord].judge
      ,[TestRecord].stress
      ,[TestRecord].WQ211
      ,[memo]
      ,[org]
      ,[createdata]
  FROM [SMTvip].[dbo].[StrainGauge]

  Left JOIN [SMTvip].[dbo].[TestRecord] 
  on [StrainGauge].[gid] = [TestRecord].[gid]
  where gpn = '{}'
  ORDER by profdate DESC
'''.format(gpn)

connection_string = "DRIVER={SQL Server};SERVER=T1-PE-SUPPORT;DATABASE=PR_WEB2;UID=pieng;PWD=Q2iT5cwHJW3FH"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
raw = pd.read_sql(strain_query, engine)

raw.judge = raw.judge.map({'OK':1, 'NG':0})
raw.sort_values('createdata', ascending=False, inplace=True)

droped = raw.drop_duplicates(subset=['PCB ver','station','Position','memo','org'])
pivot = droped.groupby(['station','memo','PCB ver','Position'])['judge'].sum().unstack('Position').sort_index(level=['station','PCB ver'],ascending=False)

with pd.ExcelWriter(getcwd()+'\{}_strain.xlsx'.format(gpn), engine='openpyxl') as writer:
    pivot.to_excel(writer, sheet_name='pivot')
    #auto_adjust_xlsx_column_width(pivot, writer, sheet_name="pivot", margin=1)

    raw.to_excel(writer, sheet_name='raw')
    auto_adjust_xlsx_column_width(raw, writer, sheet_name="raw", margin=3)