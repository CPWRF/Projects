SELECT
    SerialNumber
    ,SO
    ,Item26 Tx_avg
    ,tDateTime
    -- ,'PreMP' as phase
FROM ate_db_tblfinal_new.dbo.TblFinal f1
Where ItemNameType = 18213
and Item26St in (0,1)
-- and SO in (16628528,16628529,16628530)
and tDateTime > '2023-10-23'
-- order by SerialNumber