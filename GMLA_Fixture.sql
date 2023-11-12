SELECT
      [PROJECT_SIZE_NAME]
      ,[no]
    --   ,[questionnaire]
      ,[result]
      ,[ownerComment]
      ,[reviewerFeedBack]
      ,[reviewerUserUpdated] as 'reviewer'
      ,[pqeSummary]
      ,pqeSummaryUserupdated
      ,cast(pqeSummaryUpdatedAt as smalldatetime) pqeSummaryUpdatedAt
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST]
  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on ([T_PS_ProdSizeRelateInfo].PROJECT_SIZE_ID = [T_GMLA_CKLIST].projectSizeId)
  WHERE no in ('3.C-2')
  and pqeSummaryUpdatedAt > '2023-07-01'