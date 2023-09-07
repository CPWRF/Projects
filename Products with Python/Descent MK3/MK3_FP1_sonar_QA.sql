SELECT
    ItemNameType,
    f1.tDateTime,
    -- f1.Station,
    -- f1.StationID,
    SerialNumber,
    SO,
    case
        when SerialNumber in (3444082911, 3444082921, 3444082892) then 'drop'
        else 'tumble'
    end as ELOT,
    Item37,
    Item37St
FROM ate_db_QA.dbo.TblFinal_QA f1
where SerialNumber in (
    3444083069, 3444083087, 3444083067, /*Tumble*/
    3444082911, 3444082921, 3444082892 /*Drop*/
)
and f1.tDateTime > '2023-04-10'
and ItemNameType = 18213
order by SerialNumber, tDateTime ASC