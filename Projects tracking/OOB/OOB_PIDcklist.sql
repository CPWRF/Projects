SELECT [T_PID_CkList].[PROJECT_SIZE_ID]
      ,[Category_NameSub]
      ,[Category_Name]
      ,[ORG_FILE_NAME]
      ,[COMMENT]
      /*,[T_PID_CkList].[MpType_ID]
      ,[T_PID_CkList].[Category_ID]
      ,[T_PID_CkList].[Item_ID]*/
      ,[Item_Name]
      ,[Status]
      ,[UpdateUser]
      ,[UpdateTime]
  FROM [PR_WEB2].[dbo].[T_PID_CkList]

  LEFT JOIN [T_PID_CkListFiles]
  ON ([T_PID_CkListFiles].[PROJECT_SIZE_ID] = [T_PID_CkList].[PROJECT_SIZE_ID]
  and [T_PID_CkListFiles].[MpType_ID] = [T_PID_CkList].[MpType_ID]
  and [T_PID_CkListFiles].[Category_ID] = [T_PID_CkList].[Category_ID]
  and [T_PID_CkListFiles].[Item_ID] = [T_PID_CkList].[Item_ID]
  and [T_PID_CkListFiles].[Frequency] = [T_PID_CkList].[Frequency]
  /* Frequency is duplicated phase count (e.g. Twice FP) */)
  where Item_Name = 'OOB planning readiness' and ORG_FILE_NAME is not NULL