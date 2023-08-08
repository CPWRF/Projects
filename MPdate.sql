with CTE as (
SELECT [ProjectId]
      ,[PROJECT_SIZE_ID]
      ,[PROJECT_SIZE_NAME]
      ,CAST([CheckDate] as date) as ChangeDate
      ,RANK() OVER (PARTITION by ProjectId,PROJECT_SIZE_ID,PROJECT_SIZE_NAME ORDER by CheckDate DESC) as rnk 
      /*Rank checkdate to find latest one and it's MPdate */
      ,CAST([ChangedDate] as date) MPdate
      ,DATEADD(DAY, -7, CAST([ChangedDate] as date)) MP_CP_deadline
  FROM [PR_WEB2].[dbo].[T_MpDate_Log] mplog

  JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo] info
  ON info.[PROJECT_ID] = mplog.[ProjectId]

  WHERE PROJECT_CATEGORY != 'OEM Auto')

  /* Since rnk can't be "whered" in above query, so I create a CTE to store query result temporary and do "where" below */
  SELECT 
  ProjectId,
  PROJECT_SIZE_ID,
  PROJECT_SIZE_NAME,
  MPdate,
  MP_CP_deadline
  /* Drop "rnk" and "ChangeDate"*/
  FROM CTE
  WHERE rnk = 1 AND MPdate > '2023-08-01'
  AND PROJECT_SIZE_ID not in (1166, 1109, 1122) 
  /*Drop duplicated Descent T2, Tacx NEO 3M*, GPSMAP 9000_Black Box/
  ORDER BY MPdate