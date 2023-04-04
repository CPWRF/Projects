SELECT
    ItemNameType,
    result as 'Result',
    FailItem as 'failitem',
    SerialNumber,
    SO,
    Item70,
    Item50,
    Item63,
    Item115,
    Item89,
    Item78,
    tDateTime

from ate_db_tblfinal_new.dbo.TblFinal

WHERE SO in (16219307,
16219308,
16219309,
16219310,
16219311,
16219312,
16219313,
16219404,
16219405,
16219406,
16219407,
16219408)
and tDateTime > '2023-02-20'
and ItemNameType in (16516,16518,16521)