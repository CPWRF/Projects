SELECT [projectSizeId]
      ,[PROJECT_SIZE_NAME]
      ,[no]
      ,[questionnaire]
      ,[result]
      ,[reviewerFeedBack]
      ,[reviewerUserUpdated] as 'reviewer'
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST]
  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on ([T_PS_ProdSizeRelateInfo].PROJECT_SIZE_ID = [T_GMLA_CKLIST].projectSizeId)
  WHERE no in ('2.D-17','3.D-17')