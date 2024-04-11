-- Odd and Even Measurements
-- https://datalemur.com/questions/odd-even-measurements

with cte as (
    select
        measurement_value,
        DATE(measurement_time) as dt,
        RANK()
            over (partition by DATE(measurement_time) order by measurement_time)
        as mr
    from measurements
    group by
        DATE(measurement_time),
        measurement_id,
        measurement_value,
        measurement_time
)

select
    cte.dt as measurement_day,
    SUM(
        case when cte.mr % 2 = 0 then cte.measurement_value else 0 end
    ) as even_sum,
    SUM(
        case when cte.mr % 2 != 0 then cte.measurement_value else 0 end
    ) as odd_sum

from cte
group by cte.dt