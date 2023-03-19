SELECT [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,[ExeInfo]
      ,[Item56]
      ,[Item56St]
      ,[tDateTime]
      ,[SO]
      ,[Job_GPN]
      ,[UserName]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType = '15688'
  and tDateTime > '2022-07-18'