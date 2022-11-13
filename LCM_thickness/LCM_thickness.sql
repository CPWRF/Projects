SELECT
    Item5
    ,Item6
    ,Item7
    ,Item8
    ,SerialNumber
    ,ProductName
    ,Attribute1
    ,Shoporder
    ,tDateTime
FROM [PESupport].[dbo].[SiMachineDataTable]

WHERE ItemNameType = 8
and tDateTime BETWEEN '2022-09-01' and'2022-10-01'
and shoporder in ('16037686','16037066','16045258')
/*and SerialNumber in ('0025040400','6109530000','5909520200')*/
ORDER BY tDateTime

/*Server:T1-PE-SUPPORT*/