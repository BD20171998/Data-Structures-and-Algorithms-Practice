-- User's Third Transaction
-- https://datalemur.com/questions/sql-third-transaction

with cte as (
    select
        user_id,
        spend,
        transaction_date,
        RANK() over (partition by user_id order by transaction_date asc) as rank
    from transactions
)

select
    user_id,
    spend,
    transaction_date
from cte
where rank = 3