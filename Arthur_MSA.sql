select * from ( 
       select 
        -- SerialNumber,
        -- ItemNameType,
        -- Station,
        -- StationID,
        -- tDateTime,
        *,
        rank() over (partition by SerialNumber, Station, StationID ORDER BY tDateTime DESC) rnk
    from ate_db_QA.dbo.TblFinal_QA where SerialNumber in (
    '3437384430',
    '3437384431',
    '3437385195',
    '3437385196',
    '3437385420',
    '3437385524',
    '3437386483',
    '3437386653',
    '3437386655',
    '3437386656',
    '3437386666',
    '3437386677',
    '3437386681',
    '3437388787',
    '3437388788',
    '3437388791',
    '3437388814',
    '3437388831',
    '3437388837',
    '3437388838',
    '3437388841',
    '3437388787',
    '3437386653',
    '3437386688',
    '3437385189'
    ) ) t
where rnk <= 6

-- select 
--         (ItemNameType),
--         Station,
--         count(Station)
--     from ate_db_QA.dbo.TblFinal_QA where SerialNumber in (
--     '3437384430',
--     '3437384431',
--     '3437385195',
--     '3437385196',
--     '3437385420',
--     '3437385524',
--     '3437386483',
--     '3437386653',
--     '3437386655',
--     '3437386656',
--     '3437386666',
--     '3437386677',
--     '3437386681',
--     '3437388787',
--     '3437388788',
--     '3437388791',
--     '3437388814',
--     '3437388831',
--     '3437388837',
--     '3437388838',
--     '3437388841',
--     '3437388787',
--     '3437386653',
--     '3437386688',
--     '3437385189'
--     )
-- group by ItemNameType,Station
-- order by ItemNameType, Station