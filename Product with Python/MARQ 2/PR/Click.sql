SELECT [tDateTime]
      ,[SerialNumber]
      ,Item7 as 'Button1_ClickRatio'
      ,Item37 as 'Button4_ClickRatio'
      ,result
      ,[ProductName]
      ,[Version]
      ,[StationID]
      ,[ExeInfo]
      ,[SO]
      ,[Job_GPN]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType = '12434' 
  and tDateTime BETWEEN '2022-08-27 00:21:20' and '2022-09-01 06:55:27'
  order by tDateTime ASC