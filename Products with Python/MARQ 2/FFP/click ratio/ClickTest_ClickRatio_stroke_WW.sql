SELECT [Reference]
      ,[ItemNameType]
      ,[SerialNumber]
      ,[ProductName]
      ,Item1 as 'Button1_F1'
      ,Item3 as 'Button1_F2'
      ,[Item7] as 'Button1_ClickRatio'
      ,[Item8] as 'Button1_Stroke'
      ,Item11 as 'Button2_F1'
      ,Item13 as 'Button2_F2'
      ,[Item17] as 'Button2_ClickRatio'
      ,[Item18] as 'Button2_Stroke'
      ,Item21 as 'Button3_F1'
      ,Item23 as 'Button3_F2'
      ,[Item27] as 'Button3_ClickRatio'
      ,[Item28] as 'Button3_Stroke'
      ,Item31 as 'Button4_F1'
      ,Item33 as 'Button4_F2'
      ,[Item37] as 'Button4_ClickRatio'
      ,[Item38] as 'Button4_Stroke'
      ,Item41 as 'Button5_F1'
      ,Item43 as 'Button5_F2'
      ,[Item47] as 'Button5_ClickRatio'
      ,[Item48] as 'Button5_Stroke'
      ,[tDateTime]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('12434') 
  and tDateTime > '2022-07-21'
  and ProductName like '%Magna%'