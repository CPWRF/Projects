SELECT
    (f1.SerialNumber)
    ,SO
    ,Item19 FixtureID
    ,Item328 per9
    ,Item45 per45
    -- ,ROUND(1000*(Item95 + Item215),6) / 2 per180degree
    ,ROUND(1000*(Item95+Item125+Item155+Item185+Item215+Item245+Item275+Item305),6) / 8 per45degree
    -- ,ROUND(1000 * Item95, 6) degree0
    -- ,ROUND(1000 * Item125, 6) degree45
    -- ,ROUND(1000 * Item155, 6) degree90
    -- ,ROUND(1000 * Item185, 6) degree135
    -- ,ROUND(1000 * Item215, 6) degree180
    -- ,ROUND(1000 * Item245, 6) degree225
    -- ,ROUND(1000 * Item275, 6) degree270
    -- ,ROUND(1000 * Item305, 6) degree315
    -- ,ExeInfo
    ,f1.tDateTime
FROM ate_db_tblfinal_new.dbo.TblFinal f1
JOIN ate_db_tblfinal_new.dbo.TblFinal2 f2
ON f1.SerialNumber = f2.SerialNumber and f1.tDateTime = f2.tDateTime
JOIN ate_db_tblfinal_new.dbo.TblFinal3 f3
ON f1.SerialNumber = f3.SerialNumber and f1.tDateTime = f3.tDateTime
Where ItemNameType = 18213
-- and SO in (16628528, 16628529,16628530)
and SO in (16628528)
-- and f1.SerialNumber = 3460658790
-- and f1.SerialNumber in (3460658846,3460658917,3460658709,3460658770)
and f1.tDateTime > '2023-11-05'
-- and (Item328 < 450 and Item328 > 0)
-- and (Item45 < 450 and Item45 > 0)
and ROUND(1000*(Item95+Item125+Item155+Item185+Item215+Item245+Item275+Item305),6) / 8 < 450
-- order by SerialNumber ASC
order by ROUND(1000*(Item95+Item125+Item155+Item185+Item215+Item245+Item275+Item305),6) / 8 ASC
