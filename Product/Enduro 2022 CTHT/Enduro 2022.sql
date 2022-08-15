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
      /*
      ,[Noise]
      ,[NoiseStatus]
      ,[Signal]
      ,[SNR]
      ,[SNRStatus]
      ,[Drift]
      ,[DriftStatus]
      ,[AlmWeek]
      ,[AsicStatus]
      ,[RamRetetion]
      ,[RomTest]
      ,[RamTest]
      ,[BaseMap]
      ,[DataCard]
      ,[Btaddr2]
      ,[TestSequence]
      ,[iFixtureID]
      ,[iFixture105GPN]
      ,[Job_GPN]
      ,[ClassCode]
      */
  FROM [ate_db_tblfinal_new].[dbo].[TblFinal]

  where tDateTime BETWEEN '2022-06-24' and'2022-07-22'
  and ProductName like 'Enduro 2%'
  and ItemNameType in ('15832','15833','15834')