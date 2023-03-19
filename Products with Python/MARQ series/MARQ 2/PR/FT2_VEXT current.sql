SELECT top(2000)[TblFinal].[tDateTime]
      ,[Item180] as 'BatteryVol'
      ,[Item207] as 'VEXTcurrent'
      ,[Item207St] as 'VEXTcurrentSt'
      ,[ExeInfo]
      ,[TblFinal].[StationID]
      ,[TblFinal].[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,[SO]
      ,[Job_GPN]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  LEFT JOIN TblFinal2 on TblFinal.SerialNumber = TblFinal2.SerialNumber

  WHERE ItemNameType = '15689' 
  and TblFinal.tDateTime BETWEEN '2022-07-01' and '2022-09-06 05:16:17'
  order by BatteryVol DESC