SELECT [TblFinal].[tDateTime]
      ,[TblFinal].[StationID]
      ,[TblFinal].[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,[ExeInfo]
      ,[Item152]
      ,[Item152St]
      ,[SO]
      ,[Job_GPN]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  LEFT JOIN TblFinal2 on TblFinal.SerialNumber = TblFinal2.SerialNumber

  WHERE ItemNameType = '15688' 
  and TblFinal.tDateTime BETWEEN '2022-08-24 01:48:42' and '2022-09-06 05:16:17'
  and Item152St = '0'
  order by tDateTime ASC