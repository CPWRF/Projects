SELECT
      [PROJECT_CATEGORY] as 'segment'
      ,[PROJECT_SIZE_NAME] as 'projectName'
    --   ,[T_GMLA_CKLIST_ISSUE].[typeId]
    --   ,[T_GMLA_CKLIST_ISSUE].[id]
      ,[no] as 'No'
    --   ,[questionnaire] as 'Questionnaire'
      ,[pqeSummary] as 'issue'
      ,[plan] as 'mitigationPlan'
      ,case
        when [plan] like '%<a href%' then 1
        else 0
      end as 'prIssueHLink'
      ,CAST([submitDate] as SMALLDATETIME) as 'GMLASubmitDate'
    --   ,cast([closeDate] as smalldatetime) 'closeDate'
      ,replace([T_GMLA_CKLIST_ISSUE].updated_user,'@garmin.com','') updated_user
    --   ,[T_GMLA_CKLIST_ISSUE].[status]
    --   ,[T_GMLA_CKLIST_ISSUE].[updated_at]
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST_ISSUE]
  
  LEFT JOIN [PR_WEB2].[dbo].[T_PS_ProdSizeRelateInfo]
  on projectSizeId = PROJECT_SIZE_ID
  /* Join project names */
  
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
  
where [no] in ('2.B-5', '3.B-5')
-- and [plan] like '%<a href%'
and submitDate > '2022-09-02'
order by submitDate