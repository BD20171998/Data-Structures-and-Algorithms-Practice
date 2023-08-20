-- 607. Sales Person
-- https://leetcode.com/problems/sales-person/

select SalesPerson.name
from SalesPerson
where SalesPerson.sales_id not in 
(select Orders.sales_id from Company
inner join Orders
on Company.com_id = Orders.com_id
where Company.name = "RED") 