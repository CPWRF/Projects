SELECT [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[UserName]
      ,[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,[Item20]
      ,Item20St
      ,Item42
      ,Item42St
      ,tDateTime
      ,[SO]
      ,[Job_GPN]
      ,[ClassCode]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('15686','15687','15688') and tDateTime > '2022-07-19'