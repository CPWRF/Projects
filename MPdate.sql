with CTE as (
SELECT [ProjectId]
      ,[PROJECT_SIZE_ID]
      ,[PROJECT_SIZE_NAME]
      ,CAST([CheckDate] as date) as ChangeDate
      ,RANK() OVER (PARTITION by ProjectId,PROJECT_SIZE_ID,PROJECT_SIZE_NAME ORDER by CheckDate DESC) as rnk 
      /*Rank checkdate to find latest one and it's MPdate */
      ,CAST([ChangedDate] as date) MPdate
  FROM [PR_WEB2].[dbo].[T_MpDate_Log] mplog

  JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo] info
  ON info.[PROJECT_ID] = mplog.[ProjectId]

  WHERE PROJECT_CATEGORY != 'OEM Auto')

  /* Since rnk can't be "whered" in above query, so I create a CTE to store query result temporary and do "where" below */
  SELECT 
--   ProjectId,
--   PROJECT_SIZE_ID,
--   PROJECT_SIZE_NAME,
--   MPdate
  /* Drop "rnk" and "ChangeDate"*/
  *
  FROM CTE
  WHERE rnk = 1 and MPdate > '2023-07-01'
  ORDER BY MPdate