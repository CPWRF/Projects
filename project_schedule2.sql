SELECT 
      -- [ProjectSizeId]
      [PROJECT_CATEGORY]
      ,[PROJECT_NAME]
      -- ,[DESC_OF_TASK]
      -- ,CAST([Current_Date] as date) Date
      ,CAST(DATEADD(DAY,0,[Current_Date]) as date) MP_CP_deadline
  FROM [PR_WEB2].[dbo].[T_GT_ProjectSchedule]

  LEFT JOIN [PR_WEB2].[dbo].[T_GT_TaskBaseInfo] 
  ON [T_GT_ProjectSchedule].[TASK_ID] = [T_GT_TaskBaseInfo].TASK_ID

  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on ProjectSizeId = [T_PS_ProdSizeRelateInfo].PROJECT_SIZE_ID
  
  WHERE
  -- PROJECT_SIZE_ID = '1058' and 
  DESC_OF_TASK = 'Mass Production Begins'
  AND CAST(DATEADD(DAY,-7,[Current_Date]) as date) > '2023-08-04'
  AND PROJECT_CATEGORY != 'OEM Auto'
  order by MP_CP_deadline ASC