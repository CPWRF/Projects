SELECT [projectSizeId]
      ,LEFT([typeName],4) + Right([typeName],1) as 'Phase'
      /*,[categoryId]
      ,[no]*/
      ,[result]
  FROM [PR_WEB2].[dbo].[T_GMLA_CKLIST]
  LEFT JOIN [PR_WEB2].[dbo].[T_GMLA_BS_VERSION_TYPE]
  ON [T_GMLA_CKLIST].typeId = [T_GMLA_BS_VERSION_TYPE].id