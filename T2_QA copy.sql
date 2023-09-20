SELECT
    ItemNameType,
    f1.tDateTime,
    -- f1.Station,
    -- f1.StationID,
    SerialNumber,
    FailItem,
    UserName,
    Item4,
    Item4St,
    Item9,
    Item9St,
    Item12,
    Item12St,
    Item15,
    Item15St,
    Item16,
    Item16St,
    Item18,
    Item18St,
    Item22,
    Item22St,
    Item25,
    Item25St,
    Item28,
    Item28St,
    Item31,
    Item31St,
    Item34,
    Item34St,
    Item37,
    Item37St,
    Item43,
    Item43St
FROM ate_db.dbo.TblFinal f1
where SerialNumber in (
    3455926409,3455926292,3455926288,3455926340,3455926351,3455926347,3455926414,
    3455926343,3455926307,3455926453,3455926411,
    3455926427,3455926438,
    3455926259,3455926384,3455926281,3455926310,3455926448,
    3455926358,3455926285,3455926341,3455926391,3455926348,3455926393,3455926383,
    3455926436,3455926392,3455926317,3455926435
)
and f1.tDateTime > '2023-08-29'
-- and ItemNameType in (7041,18649,18650,18653)
and ItemNameType = 18650
order by SerialNumber, tDateTime ASC

-- SELECT
--     distinct(FailItem)
-- FROM ate_db.dbo.TblFinal f1
-- where SerialNumber in (
--     3455926409,3455926292,3455926288,3455926340,3455926351,3455926347,3455926414,
--     3455926343,3455926307,3455926453,3455926411,
--     3455926427,3455926438,
--     3455926259,3455926384,3455926281,3455926310,3455926448,
--     3455926358,3455926285,3455926341,3455926391,3455926348,3455926393,3455926383,
--     3455926436,3455926392,3455926317,3455926435
-- )
-- and f1.tDateTime > '2023-08-29'
-- -- and ItemNameType in (7041,18649,18650,18653)
-- and ItemNameType = 18650
-- -- order by SerialNumber, tDateTime ASC
-- ORDER by FailItem