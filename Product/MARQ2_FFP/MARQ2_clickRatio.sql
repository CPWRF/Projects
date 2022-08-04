SELECT [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[UserName]
      ,[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,[Item7]
      ,tDateTime
      ,[SO]
      ,[Job_GPN]
      ,[ClassCode]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('12434') 
  and tDateTime > '2022-07-19'