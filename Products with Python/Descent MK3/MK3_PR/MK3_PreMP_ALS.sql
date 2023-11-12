SELECT
    ItemNameType,
    SO,
    tDateTime,
    Item88,
    Item88St
FROM ate_db_tblfinal_new.dbo.TblFinal f1
-- JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime and f1.SerialNumber = f2.SerialNumber
where f1.SO in (
16628528, 16628529, 16628530
)
and ItemNameType = 18205