SELECT
    ItemNameType,
    f1.tDateTime,
    f1.Station,
    f1.StationID
FROM ate_db_tblfinal_new.dbo.TblFinal f1
JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime
where f1.SO in (
18192
)
and f1.tDateTime > '2023-09-05'