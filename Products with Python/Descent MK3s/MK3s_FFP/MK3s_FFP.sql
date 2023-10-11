SELECT
    ItemNameType,
    f1.tDateTime,
    f1.Station,
    f1.StationID,
    f1.SerialNumber,
    Item116,
    Item116St,
    Item117,
    Item117St,
    Item70,
    Item70St,
    Item73,
    Item73St,
    Item199,
    Item199St,
    Item64,
    Item64St,
    Item37,
    Item37St,
    Item13,
    Item13St,
    Item36,
    Item36St,
    Item43,
    Item43St,
    Item57,
    Item57St


FROM ate_db_tblfinal_new.dbo.TblFinal f1
JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime and f1.SerialNumber = f2.SerialNumber
where f1.SO in (
16401717,
16401718,
16401719,
16401720,
16401721,
16401722,
16401723,
16401724,
16401725,
16401726,
16401727,
16401728,
16401729,
16401731,
16401733,
16401735,
16401737,
16401739,
16401741,
16408456,
16408650,
16408651
)
and f1.tDateTime > '2023-07-30'
and ItemNameType in (
    18191,
    18192,
    18195,
    18200,
    18205,
    18213
)