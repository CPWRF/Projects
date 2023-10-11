select SerialNumber, Tumble_Cycle, tDate, ROUND(AVG(Item37),2) Sonar_Tx_RMS_AVG from (
    SELECT
        SerialNumber,
        cast(tDateTime as date) tDate,
        case
            when cast(tDateTime as date) = '2023-09-21' then 0
            when cast(tDateTime as date) = '2023-09-22' then 40
            when cast(tDateTime as date) = '2023-09-23' then 70
            when cast(tDateTime as date) = '2023-09-25' then 100
            else null
        end Tumble_Cycle,
        Item37
    FROM ate_db_tblfinal_new.dbo.TblFinal f1
    -- JOIN [dbo].[TblFinal2] f2 on f1.tDateTime = f2.tDateTime
    where SerialNumber in (3457337206, 3457337467, 3457337449 ) /*Tumble*/
    and f1.tDateTime > '2023-04-10'
    and ItemNameType = 18213
    and UserName = 3622
    and Item37St = 1
    -- order by SerialNumber, cast(tDateTime as date) ASC
) t
group by SerialNumber, Tumble_Cycle, tDate
order by SerialNumber, Tumble_Cycle