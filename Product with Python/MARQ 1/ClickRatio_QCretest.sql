SELECT [tDateTime]
      ,[SerialNumber]
      ,[Result]
      ,[FailItem]
      ,[UserName]
      ,[Item7] as 'Btn1_ClickRatio'
      ,[Item17] as 'Btn2_ClickRatio'
      ,[Item27] as 'Btn3_ClickRatio'
      ,[Item37] as 'Btn4_ClickRatio'
      ,[Item47] as 'Btn5_ClickRatio'
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  WHERE ItemNameType = 9288
  and tDateTime > '2020-07-28'
  and UserName in ('0167','4176','4892')
  and FailItem in ('0','7','17','27','37','47')
  order by tDateTime, SerialNumber ASC