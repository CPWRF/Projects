select
    TblFinal2.tDateTime,
    TblFinal2.SerialNumber,
    ProductName,
    Item152,
    Item152St
from ate_db_tblfinal_new.dbo.TblFinal2

Join ate_db_tblfinal_new.dbo.TblFinal on TblFinal.SerialNumber = TblFinal2.SerialNumber

where ItemNameType = 15687
and TblFinal2.tDateTime > '2022-10-12'
and Item152St in (0,1)
and Item152 != 0
order by tDateTime, SerialNumber ASC