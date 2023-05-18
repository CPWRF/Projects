SELECT
    ItemNameType,
    ProductName,
    SerialNumber,
    Item12,
    tDateTime

From ate_db_QA.dbo.TblFinal_QA

WHERE SO = 16300370
and tDateTime > '2023-04-15'
and ItemNameType in (17936)
and SerialNumber != '1111111111'
and (Item12St = 1)
order by SerialNumber DESC