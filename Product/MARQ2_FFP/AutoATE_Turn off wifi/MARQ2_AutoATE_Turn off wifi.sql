SELECT [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[SerialNumber]
      ,[ProductName]
      ,[Item121]
      ,[Item121St]
      ,[ExeInfo]
      ,[tDateTime]
  FROM [ate_db_tblcpu].[dbo].[TblCpu]

  /*Where ProductName like 'MARQ%GEN2%'*/
  Where ItemNameType = '15545'
  and Item121St in (0,1)
  and tDateTime > '2022-06-20'
  ORDER by tDateTime ASC