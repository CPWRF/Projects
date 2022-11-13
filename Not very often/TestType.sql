SELECT
    DISTINCT
    ate_db_tblfinal_new.dbo.TblFinal.TestType,
    ate_db_tblfinal_new.dbo.TblFinal.TestType2,
    Purpose,
    left(Job_GPN,10)
    
FROM ate_db_tblfinal_new.dbo.TblFinal
left join [ate_result].[dbo].[xx_TestTypeList] 
on (ate_db_tblfinal_new.dbo.TblFinal.TestType2 = [ate_result].[dbo].[xx_TestTypeList].TestType2
and ate_db_tblfinal_new.dbo.TblFinal.TestType = [ate_result].[dbo].[xx_TestTypeList].TestType)

where tDateTime > '2022-10-01'
and Job_GPN like '010-02648-__'
ORDER by TestType2

