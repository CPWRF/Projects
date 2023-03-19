SELECT [tDateTime]
      ,[SerialNumber]
      ,[ProductName]
      ,[Result]
      ,[Item7] as 'Button1_ClickRatio'
      ,[Item17] as 'Button2_ClickRatio'
      ,[Item27] as 'Button3_ClickRatio'
      ,[Item37] as 'Button4_ClickRatio'
      ,[Item47] as 'Button5_ClickRatio'
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType = 9288
  and Result = 1
  and tDateTime > '2020-07-28'
  order by tDateTime, SerialNumber ASC