SELECT [Reference]
      ,[ItemNameType]
      ,[SerialNumber]
      ,[ProductName]
      ,[Item7] as 'Button1_ClickRatio'
      ,[Item17] as 'Button2_ClickRatio'
      ,[Item27] as 'Button3_ClickRatio'
      ,[Item37] as 'Button4_ClickRatio'
      ,[Item47] as 'Button5_ClickRatio'
      ,[Item8] as 'Button1_Stroke'
      ,[Item18] as 'Button2_Stroke'
      ,[Item28] as 'Button3_Stroke'
      ,[Item38] as 'Button4_Stroke'
      ,[Item48] as 'Button5_Stroke'
      ,[tDateTime]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('12434') 
  and tDateTime > '2022-07-21'
  and ProductName like '%Magna%'