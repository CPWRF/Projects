SELECT
    ItemNameType,
    ProductName,
    Item16,
    Item16St,
    Item85,
    Item85St,
    Item14,
    Item14St,
    Item45,
    Item45St
    Item15,
    Item15St,
    Item51,
    Item51St,
    tblfinal.tDateTime

FROM ate_db_tblfinal_new.dbo.TblFinal

JOIN dbo.tblfinal2 on
(tblfinal.tDateTime = tblfinal2.tDateTime 
and tblfinal.SerialNumber = tblfinal2.SerialNumber)

WHERE tblfinal.tDateTime > '2023-03-16'
and ItemNameType in (13602, 7041, 13616, 19448)