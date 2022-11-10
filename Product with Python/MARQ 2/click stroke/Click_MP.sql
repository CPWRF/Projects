SELECT [SerialNumber]
      ,[tDateTime]
      ,ProductName
      ,result
      ,FailItem
      ,[Item7] as 'Btn1_click'
      ,[Item17] as 'Btn2_click'
      ,[Item27] as 'Btn3_click'
      ,[Item37] as 'Btn4_click'
      ,[Item47] as 'Btn5_click'
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType in ('18058')
  and FailItem in (0,7,17,27,37,47)
  and tDateTime > '2022-10-28'

  order by tDateTime, SerialNumber ASC