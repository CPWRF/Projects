SELECT
    ItemNameType,
    f1.tDateTime,
    f1.Station,
    f1.StationID,
    Item150,
    Item150St,
    Item28,
    Item28St,
    Item30,
    Item30St,
    -- Item156,
    -- Item156St,
    Item89,
    Item89St,
    Item60,
    Item60St
FROM ate_db_tblfinal_new.dbo.TblFinal f1
-- JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime
where f1.SO in (
16382236,
16382237,
16382238,
16382239,
16382240,
16382241,
16382242,
16382243,
16382244,
16382245,
16382246,
16382247,
16383894,
16404199,
16404200,
16404201,
16404206,
16404267
)
and f1.tDateTime > '2023-07-10'