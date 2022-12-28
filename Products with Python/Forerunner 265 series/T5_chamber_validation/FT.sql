SELECT
    ItemNameType
    ,TblFinal.SerialNumber
    ,Item195 as 'L1byRef(Item195)'
    ,Item187 as 'L5byRef(Item187)'
    ,TblFinal.Station
    ,TblFinal.stationID
    ,TblFinal.tDateTime
FROM ate_db_tblfinal_new.dbo.TblFinal

JOIN ate_db_tblfinal_new.dbo.TblFinal2 
on (TblFinal2.SerialNumber = TblFinal.SerialNumber
and TblFinal2.tDateTime = TblFinal.tDateTime
)

where TblFinal.UserName = 7924
and ItemNameType = 16919
and TblFinal.tDateTime between '2022-11-23 09:54' and '2022-11-26'
and TblFinal.SerialNumber = 3434048539