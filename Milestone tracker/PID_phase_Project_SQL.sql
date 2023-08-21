DECLARE @WP_FRM178 VARCHAR(50)='Working Prototype Form 178 Submitted'
DECLARE @FFP_FRM178 VARCHAR(50)='Final Factory Form 178 Submitted'
DECLARE @PR_FRM178 VARCHAR(50)='Pilot Run Form 178 Submitted'
DECLARE @FP_DR VARCHAR(50)='Factory Prototype Design Review'
DECLARE @PR_DR VARCHAR(50)='Pilot Run Design Review'
DECLARE @MPB VARCHAR(50)='Mass_production_Begins'

SELECT PS.ProjectSizeId,PSR.PROJECT_NAME,TBI.DESC_OF_TASK,
CASE 
      WHEN TBI.DESC_OF_TASK = @WP_FRM178 THEN DATEADD(DAY,42,CAST(PS.[Current_Date] AS DATE))
      WHEN TBI.DESC_OF_TASK = @FFP_FRM178 OR
      TBI.DESC_OF_TASK = @PR_FRM178 THEN DATEADD(DAY,7,CAST(PS.[Current_Date] AS DATE))
      WHEN TBI.DESC_OF_TASK = @FP_DR OR 
      TBI.DESC_OF_TASK = @PR_DR THEN DATEADD(DAY,-21,CAST(PS.[Current_Date] AS DATE))
      WHEN TBI.DESC_OF_TASK = @MPB THEN DATEADD(DAY,-7,CAST(PS.[Current_Date] AS DATE))
      ELSE CAST(PS.[Current_Date] AS DATE)
   END AS DATE,
CASE 
      WHEN TBI.DESC_OF_TASK = @WP_FRM178 THEN  'DFM,WP_GMLA'           
      WHEN TBI.DESC_OF_TASK = @FFP_FRM178 THEN 'FP_CP,FP_4M,FP_PW'
      WHEN TBI.DESC_OF_TASK = @PR_FRM178 THEN 'PR_CP,PR_4M,PR_PW'
      WHEN TBI.DESC_OF_TASK = @FP_DR THEN 'FP_GMLA'
      WHEN TBI.DESC_OF_TASK = @PR_DR THEN 'PR_GMLA'     
      WHEN TBI.DESC_OF_TASK = @MPB THEN 'Handover'
      ELSE ''
   END AS DPQE_Task,
CASE 
      WHEN TBI.DESC_OF_TASK = @WP_FRM178 THEN  'Detail Design Close Meeting'
      WHEN TBI.DESC_OF_TASK = @FFP_FRM178 THEN 'Factory Prototype Kick off Meeting'
      WHEN TBI.DESC_OF_TASK = @PR_FRM178 THEN 'Pilot Run Kick off Meeting'
      WHEN TBI.DESC_OF_TASK = @FP_DR THEN 'Factory Prototype Close Meeting'
      WHEN TBI.DESC_OF_TASK = @PR_DR THEN 'Pilot Run Close Meeting'     
      WHEN TBI.DESC_OF_TASK = @MPB THEN ''
      ELSE ''
   END AS Alternative

  FROM [PR_WEB2].[dbo].[T_GT_ProjectSchedule] AS PS
  INNER JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo] 
  AS PSR ON PS.ProjectSizeId=PSR.PROJECT_SIZE_ID
  INNER JOIN [PR_WEB2].[dbo].[T_GT_TaskBaseInfo] 
  AS TBI ON PS.[TASK_ID]=TBI.[TASK_ID]
  WHERE PS.[ProjectSizeId]=1057 and PSR.PROJECT_NAME='Descent Mk3 Series'
  ORDER BY PS.[Current_Date]

