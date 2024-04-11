-- Supercloud Customer
-- https://datalemur.com/questions/supercloud-customer

with cte as (
    select
        customer_contracts.customer_id,
        products.product_category,

        count(products.product_category)
            over (partition by customer_contracts.customer_id)
        as ct
    from customer_contracts
    inner join products
        on customer_contracts.product_id = products.product_id

    group by
        customer_id,

        products.product_category

    order by customer_id
)

select distinct cte.customer_id from cte

where cte.ct = 3
