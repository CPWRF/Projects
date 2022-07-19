SELECT [T_GMLA_CKLIST].[projectSizeId]
      ,[PROJECT_SIZE_NAME]
      ,[typeName]
      ,[no]
      ,[categoryName]
      ,[riskType]
      ,[result]
      ,[kickOffMeetingDate]
      ,[baseOverDueDate] as 'closeMeetingDate'
      ,[submitDate] as 'GMLASubmitDate'
      ,[rejectReason]
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST]
  
  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on projectSizeId = PROJECT_SIZE_ID
  /* Join project names */
  
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE]
  ON typeId = [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE].id
  /* Join GMLA#1/#2/#3 name*/
  
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_CKLIST_CONFIRM]
  ON ([T_GMLA_CKLIST].projectSizeId = [T_GMLA_CKLIST_CONFIRM].projectSizeId 
  and [T_GMLA_CKLIST].typeId = [T_GMLA_CKLIST_CONFIRM].typeId)
  /* Join close meeting date and GMLA submit date */

  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_CATEGORY]
  ON [T_GMLA_CKLIST].categoryId=[T_GMLA_BS_CATEGORY].id
  /* Join 6 category name via id */

  WHERE [result] != '0'
  /* Select completed GMLA */