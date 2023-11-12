SELECT
    DISTINCT(SerialNumber),
    -- (f1.tDateTime),
    first_value(Item37) over (PARTITION by SerialNumber order by tDateTime DESC) Tx_avg,
    'PR' as phase
FROM ate_db_tblfinal_new.dbo.TblFinal f1
Where ItemNameType = 18213
and Item37St in (0,1)
and so in (
    16500958,
16500959,
16500960,
16500961,
16500962,
16513963,
16513964,
16513965,
16513966,
16513967,
16513968,
16513969,
16513970,
16513971,
16513972,
16513973,
16513974,
16513975
)
order by SerialNumber