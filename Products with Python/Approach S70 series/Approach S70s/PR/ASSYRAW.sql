SELECT
    ItemNameType,
    ProductName,
    result,
    FailItem,
    SerialNumber,
    SO,
    Item57,
    Item45,
    Item47,
    Item46,
    tDateTime

from ate_db_tblfinal_new.dbo.TblFinal

WHERE SO in (16199731,
16199732,
16199733,
16199784,
16199785,
16199786,
16213153,
16213184,
16213185,
16218526,
16218527,
16218528
)
and tDateTime > '2023-02-20'
and ItemNameType in (16528,
16521,
16519,
18267,
16519,
16521,
16516,
16518,
16199
)