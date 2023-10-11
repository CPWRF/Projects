SELECT
    ItemNameType,
    f1.tDateTime,
    -- f1.Station,
    -- f1.StationID,
    SerialNumber,
    SO,
    case
        when SO = 16383894 then '2.5mm'
        else '2.0mm'
    end as Thickness,
    Item37,
    Item37St
FROM ate_db_tblfinal_new.dbo.TblFinal f1
-- JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime
where f1.SO in (
16383894,
16404199
)
and f1.tDateTime > '2023-07-10'
and ItemNameType = 18213