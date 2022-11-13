SELECT [ItemNameType] 
      ,[SerialNumber]
      ,[Job_GPN]
      ,[ProductName]
      ,[Item7]
      ,[tDateTime]
      ,[SO]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('12434') 
  and tDateTime BETWEEN '2022-07-19' and '2022-08-01'
  and ProductName like '%Magna%'