SELECT [T_MPC_CkListInfo].[PROJECT_SIZE_ID]
      ,[PROJECT_NAME]
      /*,[T_MPC_CkListInfo].[MP_ID]
      ,[T_MPC_CkListInfo].[Item_ID]*/
      ,[Item_Name] as 'Description'
      ,[ORG_FILE_NAME] as 'Uploaded file name'
      ,[Comment] /* User comment */
      ,[Status] /* If item is checked, 1=checked, 2=N/A */
      ,[UpdateUser]
      ,[UpdateTime]
  FROM [PR_WEB2].[dbo].[T_MPC_CkListInfo]

  LEFT JOIN [dbo].[T_PS_ProdSizeRelateInfo] 
  on [T_MPC_CkListInfo].PROJECT_SIZE_ID = [T_PS_ProdSizeRelateInfo].PROJECT_SIZE_ID

  LEFT JOIN [dbo].[T_MPC_RefFiles] on 
    [T_MPC_CkListInfo].PROJECT_SIZE_ID = [T_MPC_RefFiles].PROJECT_SIZE_ID
    AND [T_MPC_CkListInfo].MP_ID = [T_MPC_RefFiles].MP_ID
    AND [T_MPC_CkListInfo].Item_ID = [T_MPC_RefFiles].Item_ID
    /* Merge uploaded file name */

  where Item_Name like 'OOB%'
  /* Item_Name is 'Descroption' in MP information */
 
  ORDER BY [UpdateTime] DESC