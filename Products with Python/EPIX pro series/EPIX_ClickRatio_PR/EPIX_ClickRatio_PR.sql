SELECT
    ProductName,
    Job_GPN,
    SerialNumber,
    tDateTime,
    Result,
    FailItem,
    Item7,
    Item17,
    Item27,
    Item37,
    Item47

FROM ate_db_tblfinal_new.dbo.TblFinal

WHERE ItemNameType = '12434' and tDateTime > '2022-12-01' and Job_GPN like '010-0280_-__'
ORDER BY tDateTime DESC