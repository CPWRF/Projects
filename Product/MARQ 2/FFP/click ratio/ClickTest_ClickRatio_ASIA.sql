SELECT [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[UserName]
      ,[SerialNumber]
      ,[ProductName]
      ,[Item7] as 'Button1_ClickRatio'
      ,[Item17] as 'Button2_ClickRatio'
      ,[Item27] as 'Button3_ClickRatio'
      ,[Item37] as 'Button4_ClickRatio'
      ,[Item47] as 'Button5_ClickRatio'
      ,[tDateTime]
      ,[SO]
      ,[Job_GPN]
      ,[ClassCode]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('12434') 
  and tDateTime > '2022-08-04'
  and ProductName like '%Magna%'