SELECT
    -- ItemNameType,
    -- f1.SerialNumber,
    -- f1.tDateTime,
    -- f1.Station,
    -- f1.StationID,
    Item21 as FixtureID,
    count(*) n_count
FROM ate_db_tblcpu.dbo.TblCpu
-- JOIN [dbo].[TblFinal2] f2 on f1.SerialNumber = f2.SerialNumber and f1.tDateTime = f2.tDateTime
where ItemNameType = 18323
and tDateTime > '2023-10-01'
group by Item21