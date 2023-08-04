SELECT
    ItemNameType,
    result as 'Result',
    FailItem as 'failitem',
    TblFinal.SerialNumber,
    SO,
    Item58,
    Item90,
    Item173,
    TblFinal.tDateTime

from ate_db_tblfinal_new.dbo.TblFinal

JOIN ate_db_tblfinal_new.dbo.TblFinal2 
on (TblFinal.tDateTime = TblFinal2.tDateTime
and TblFinal.SerialNumber = TblFinal2.SerialNumber)

WHERE SO in (16164259,
16164260,
16164261,
16164262,
16164263,
16164264,
16164275,
16164276,
16164277,
16164278,
16164279,
16164280,
16164282,
16213672,
16213673,
16213694,
16217058,
16217079
)
and TblFinal.tDateTime > '2023-02-01'
and ItemNameType in (15686,15688,15545)