SELECT [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[UserName]
      ,[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,[Item33]
      ,Item33St
      ,tDateTime
      ,[SO]
      ,[Job_GPN]
      ,[ClassCode]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType = '17466'
  and tDateTime > '2022-07-19'