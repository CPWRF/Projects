SELECT /*[T_GMLA_CKLIST_ISSUE].[projectSizeId]*/
      [riskType] as 'Risk'
      ,[PROJECT_CATEGORY] as 'Segment'
      ,[PROJECT_SIZE_NAME] as 'Project Name'
      /*,[T_GMLA_CKLIST_ISSUE].[typeId]*/
      ,[typeName] as 'Phase'
      ,[submitDate] as 'GMLA Submit Date'
      /*,[T_GMLA_CKLIST_ISSUE].[categoryId]*/
      ,[categoryName] as 'Category'
      /*,[T_GMLA_CKLIST_ISSUE].[id]*/
      ,[no] as 'No'
      ,[questionnaire] as 'Questionnaire'
      ,[pqeSummary] as 'Reason'
      ,[plan]
      ,[issueOwner]
      ,[targetDate]
      ,[closeDate]
      ,[T_GMLA_CKLIST_ISSUE].[status]
      /*,[T_GMLA_CKLIST_ISSUE].[updated_at]*/
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST_ISSUE]
  
  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on projectSizeId = PROJECT_SIZE_ID
  /* Join project names */
  
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE]
  ON typeId = [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE].id
  /* Join GMLA#1/#2/#3 name*/
  
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_CATEGORY]
  ON [T_GMLA_CKLIST_ISSUE].categoryId=[T_GMLA_BS_CATEGORY].id
  /* Join 6 category name via id */

  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_CKLIST_CONFIRM]
  ON ([T_GMLA_CKLIST_ISSUE].projectSizeId = [T_GMLA_CKLIST_CONFIRM].projectSizeId
  AND [T_GMLA_CKLIST_ISSUE].typeId = [T_GMLA_CKLIST_CONFIRM].typeId)
  /* Join GMLA submit date */

  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_CKLIST]
  ON ([T_GMLA_CKLIST_ISSUE].[categoryId] = [T_GMLA_CKLIST].[categoryId]
  AND [T_GMLA_CKLIST_ISSUE].id = [T_GMLA_CKLIST].id
  AND [T_GMLA_CKLIST_ISSUE].projectSizeId = [T_GMLA_CKLIST].projectSizeId
  AND [T_GMLA_CKLIST_ISSUE].typeId = [T_GMLA_CKLIST].typeId)
  /* Join serval datas */