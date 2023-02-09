SELECT
    ProductName
    ,ItemNameType
    ,SerialNumber
    ,SO
    ,Result
    ,tDateTime
    ,UserName
FROM ate_db_tblfinal_new.dbo.TblFinal

WHERE tDateTime > '2022-10-04'
and SO in ('16050826','16050829')
and ItemNameType in ('14394')
and Result = 1

ORDER BY tDateTime, SerialNumber ASC