-- 1068. Product Sales Analysis I
-- https://leetcode.com/problems/product-sales-analysis-i/

select
        product_name,
        year,
        price 
    from
        Product 
    inner join
        Sales 
            on Product.product_id = Sales.product_id