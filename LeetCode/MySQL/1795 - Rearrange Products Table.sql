-- 1795. Rearrange Products Table
-- https://leetcode.com/problems/rearrange-products-table/

select product_id, "store1" as store, store1 as price
from Products
WHERE store1 IS NOT NULL 
union
select product_id, "store2" as store, store2 as price
from Products
WHERE store2 IS NOT NULL 
union
select product_id, "store3" as store, store3 as price
from Products
WHERE store3 IS NOT NULL 