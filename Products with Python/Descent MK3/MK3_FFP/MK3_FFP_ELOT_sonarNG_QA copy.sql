SELECT
    ItemNameType,
    f1.tDateTime,
    -- f1.Station,
    -- f1.StationID,
    SerialNumber,
    SO,
    FailItem,
    Item37,
    Item37St
FROM ate_db_QA.dbo.TblFinal_QA f1
where SerialNumber in (
    	3452787503
)
and f1.tDateTime > '2023-04-10'
and ItemNameType = 18213
order by SerialNumber, tDateTime ASC