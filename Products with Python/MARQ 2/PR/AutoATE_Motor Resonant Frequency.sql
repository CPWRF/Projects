SELECT [tDateTime]
      ,[ItemNameType]
      ,[StationID]
      ,[SerialNumber]
      ,[ProductName]
      ,[Item58]
      ,[Item58St]
      ,[SO]
      ,[Job_GPN]
  FROM [ate_db_tblcpu].[dbo].[TblCpu]
  WHERE ItemNameType = 15545
  and tDateTime BETWEEN '2022-08-11 10:56:50.14' and '2022-08-22 02:42:58.35'
  and Item58St in (0,1)
  ORDER BY tDateTime ASC