SELECT TOP (1000) [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[UserName]
      ,[SerialNumber]
      ,[ProductName]
      ,[tDateTime]
      ,[Job_GPN]
  FROM [ate_db_QA].[dbo].[TblFinal_QA]

  where ItemNameType = '17369' 
  and tDateTime>'2022-07-18'
  and SerialNumber = '1111111111'
  order by tDateTime ASC