SELECT
    cpu1.SerialNumber
    ,cpu1.tDateTime
    ,Item151
    ,Item151St
    ,Item152
    ,Item152St
    ,Result
    ,CASE
        when SO in (16500955, 16500956, 16500957) then 'PR'
        when cpu1.tDateTime > '2023-10-18' then 'PreMp'
        else null
    END as phase
FROM ate_db_tblcpu.dbo.TblCpu cpu1
JOIN ate_db_tblcpu.dbo.TblCpu2 cpu2 on cpu1.SerialNumber = cpu2.SerialNumber and cpu1.tDateTime = cpu2.tDateTime
where ItemNameType = 18322 
and cpu1.tDateTime > '2023-08-28'
and ProductName like '%51MM%'
and Result = 1