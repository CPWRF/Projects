SELECT [Reference]
      ,[ItemNameType]
      ,[StationID]
      ,[SerialNumber]
      ,[ProductName]
      ,[Version]
      ,Item80 as 'CT GPS_(L1+L5) by ref'
      ,Item80St as 'CT GPS_(L1+L5) by ref st'
      ,Item91 as 'HT GPS_L5 by ref'
      ,Item91St as 'HT GPS_L5 by ref st'
      ,Item48 as 'FT GPS_(L1+L5) by ref'
      ,Item48St as 'FT GPS_(L1+L5) by ref st'
      ,[tDateTime]
      ,[Temperature]
      ,[SO]
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  where tDateTime > '2022-06-24'
  and ProductName like 'Enduro 2%'
  and ItemNameType in ('15832','15833','15834')
  ORDER BY tDateTime ASC