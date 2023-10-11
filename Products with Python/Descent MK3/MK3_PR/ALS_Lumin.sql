SELECT [Station],[ExeInfo],[tDateTime],
  -- Item43 CTP, 
  -- Item44 NFC_Init, 
  -- Item45 NFC_CRS, 
  -- Item46 NFC_ANT, 
  Item47 ALS_Lumin,
  Item47St,
  [SerialNumber]
FROM ate_db.dbo.TblCleanroom
where tDateTime > '2023-09-01'
and ItemNameType = '19000'
and shoporder = '16500949'
-- and ExeInfo like'%MK3%'
--    and NOHGPN = '011-05977-21'
  -- and attribute1='LMCW1456'