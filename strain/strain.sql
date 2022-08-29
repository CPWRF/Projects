SELECT  [StrainGauge].[gid]
      ,[gpn]
      ,[ver] as 'PCB ver'
      ,[toolno]
      ,[station]
      ,[Position]
      ,[TestRecord].judge
      ,[TestRecord].stress
      ,[TestRecord].WQ211
      ,[memo]
      ,[org]
      ,[profdate]
      ,[createdata]
  FROM [SMTvip].[dbo].[StrainGauge]

  Left JOIN [SMTvip].[dbo].[TestRecord] 
  on [StrainGauge].[gid] = [TestRecord].[gid]
  
  where createdata > '2020-01-01'
  
  ORDER by profdate DESC