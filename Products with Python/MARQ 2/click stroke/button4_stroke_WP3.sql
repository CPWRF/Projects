SELECT [Reference]
      ,[ItemNameType]
      ,[Item38]
      ,[failitem]
      ,[tDateTime]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('12434') 
  and tDateTime BETWEEN '2021-12-09' and '2021-12-11'