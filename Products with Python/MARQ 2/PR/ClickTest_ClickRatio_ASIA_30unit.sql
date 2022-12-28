SELECT [tDateTime]
      ,[SerialNumber]
      ,[ProductName]
      ,result
      ,[Item7] as 'Button1_ClickRatio'
      ,[Item17] as 'Button2_ClickRatio'
      ,[Item27] as 'Button3_ClickRatio'
      ,[Item37] as 'Button4_ClickRatio'
      ,[Item47] as 'Button5_ClickRatio'
      ,[Job_GPN]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('18058')
  and tDateTime > '2022-11-11'
  and result = 1
  order by tDateTime, SerialNumber ASC