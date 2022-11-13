SELECT TOP (1000) [Reference]
      ,[ItemNameType]
      ,Station
      ,[StationID]
      ,[UserName]
      ,[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,ExeInfo
      ,[Item117]
      ,[Item117St]
      ,[SO]
      ,[Job_GPN]
      ,tDateTime
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

   where ItemNameType = '16619'
   and tDateTime BETWEEN '2022-08-01' and '2022-08-20'