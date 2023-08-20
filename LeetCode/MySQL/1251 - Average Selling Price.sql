-- 1251. Average Selling Price
-- https://leetcode.com/problems/average-selling-price/

select Prices.product_id, 
    round(sum(Prices.price*UnitsSold.units)/sum(UnitsSold.units),2) as average_price
from Prices
inner join UnitsSold
where Prices.product_id = UnitsSold.product_id
and (UnitsSold.purchase_date between Prices.start_date and  Prices.end_date)
group by Prices.product_id