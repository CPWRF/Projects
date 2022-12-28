SELECT
    ItemNameType
    ,TblFinal.tDateTime
    ,TblFinal.SerialNumber
    ,Item46 as 'CT_GPS_ (L1 only) by ref'
    ,Item46St
    ,Item89 as 'FT1_GPS_ (L1 only) by ref_BL1'
    ,Item89St
    ,Item42 as 'HT_GPS_ (L1 only) by ref'
    ,Item42St
    ,Item189 as 'FT2_NFC Test'
    ,Item189St
    ,Item147 as 'FT2_ANT Radiated TX'
    ,Item147St

FROM dbo.TblFinal

JOIN dbo.TblFinal2 on (TblFinal.SerialNumber = TblFinal2.SerialNumber)

where TblFinal.tDateTime BETWEEN '2022-10-28 10:37:01' and '2022-11-15 09:24:02'
AND ItemNameType in (16550,16557,16551,16558,16554)