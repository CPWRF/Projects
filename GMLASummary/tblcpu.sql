SELECT TOP (1000)
      [ItemNameType]
      ,[UserName]
      ,[TblCpu].[SerialNumber]
      ,[TblCpu].[ProductName]
      ,[AddTotal].ProductName as 'GPN'
      ,[SMD_Job]
      ,[Add10] as 'ASSY_JOB'
      ,[TestType]
      ,[FinalIndex]
      ,[TestType2]
      ,[FailMode]
      ,[DetailResult]
      ,[ExeInfo]
      ,[ProductID]
      ,[SW_Version]
      ,[BtAddr]
      ,[DigitalID]
      ,[AsicTest]
      ,[BrvoTest]
      ,[EthernetTest]
      ,[MAC_address]
      ,[EthernetAddr]
      ,[Btaddr2]
      ,[iFixtureID]
      ,[iFixture105GPN]
      ,[SO]
      ,[Job_GPN]
      ,[ClassCode]
  FROM [ate_db_tblcpu].[dbo].[TblCpu]

  LEFT JOIN [ate_result].[dbo].[AddTotal]
  ON [TblCpu].[SerialNumber] = [AddTotal].[SerialNumber]
  /* Get ASSY job order from bundle table */

  LEFT JOIN [ate_db].[dbo].[ESN_Jobs]
  ON [TblCpu].[SerialNumber] = [ESN_Jobs].[ESN]
  /* Get SMD job order */