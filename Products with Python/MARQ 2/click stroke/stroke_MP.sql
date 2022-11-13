SELECT [SerialNumber]
      ,[Item8] as 'Button1_Stroke'
      ,[Item18] as 'Button2_Stroke'
      ,[Item28] as 'Button3_Stroke'
      ,[Item38] as 'Button4_Stroke'
      ,[Item48] as 'Button5_Stroke'
      ,result
      ,[tDateTime]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('18058') 
  and tDateTime > '2022-10-01'