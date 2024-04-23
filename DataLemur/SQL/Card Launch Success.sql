-- Card Launch Success
-- https://datalemur.com/questions/card-launch-success

with cte as (
    select
        *,
        RANK() over (
            partition by card_name
            order by
                issue_year asc,
                issue_month asc
        ) as myrank

    from monthly_cards_issued

    group by card_name, id
    order by
        card_name asc,
        issue_year asc,
        issue_month asc
)

select
    card_name,
    issued_amount

from cte
where myrank = 1
order by issued_amount desc