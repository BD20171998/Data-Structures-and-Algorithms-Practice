-- Highest-Grossing Items
-- https://datalemur.com/questions/sql-highest-grossing

with cte as (
    select
        category,
        product,
        sum(spend) --OVER (PARTITION BY category, product)
        as total_spend,
        rank() over (partition by category order by sum(spend) desc)
        as ranks
    from product_spend

    where transaction_date between '2022-01-01' and '2022-12-31'
    group by category, product
    order by category, product
)

select
    category,
    product,
    total_spend
from cte

where ranks <= 2
order by category asc, total_spend desc