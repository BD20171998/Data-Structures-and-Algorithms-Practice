-- Histogram of Users and Purchases
-- https://datalemur.com/questions/histogram-users-purchases

with cte as (
    select

        *,
        RANK() over (
            partition by user_id
            order by transaction_date desc
        ) as myrank

    from user_transactions

    group by user_id, user_transactions.id

    order by user_id--,transaction_date DESC

)

select
    cte.transaction_date,
    cte.user_id,
    COUNT(cte.user_id) as purchase_count
from cte
where cte.myrank = 1
group by
    cte.user_id,
    cte.transaction_date

order by cte.transaction_date asc