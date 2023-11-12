SELECT
    f1.SerialNumber
    -- ,SO
    ,CASE f1.SerialNumber
        When 3460658709 then 'ground'
        When 3460658846 then 'cracked_w_label'
        When 3460658770 then 'good_sample'
        when 3460658917 then 'cracked_w/o_label'
    END sample_status
    ,Item19 FixtureID
    ,ExeInfo
    ,Item45 Tx_avg
    ,(Item95+Item125+Item155+Item185+Item215+Item245+Item275+Item305)/8
    ,ROUND(1000*Item95, 6) degree0
    ,ROUND(1000 * Item125, 6) degree45
    ,ROUND(1000 * Item155, 6) degree90
    ,ROUND(1000 * Item185, 6) degree135
    ,ROUND(1000 * Item215, 6) degree180
    ,ROUND(1000 * Item245, 6) degree225
    ,ROUND(1000 * Item275, 6) degree270
    ,ROUND(1000 * Item305, 6) degree315
    -- ,f1.tDateTime
FROM ate_db_QA.dbo.TblFinal_QA f1 
JOIN ate_db_QA.dbo.TblFinal2_QA f2
ON f1.SerialNumber = f2.SerialNumber and f1.tDateTime = f2.tDateTime
JOIN ate_db_QA.dbo.TblFinal3_QA f3
ON f1.SerialNumber = f3.SerialNumber and f1.tDateTime = f3.tDateTime
Where ItemNameType = 18213
and f1.SerialNumber in (3460658846,3460658917,3460658709,3460658770)
and f1.tDateTime > '2023-11-05'
and Item45 != 0
order by SerialNumber, FixtureID