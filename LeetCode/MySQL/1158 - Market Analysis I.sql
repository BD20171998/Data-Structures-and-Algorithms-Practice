#1158. Market Analysis I
#https://leetcode.com/problems/market-analysis-i/
select
  user_id as "buyer_id" ,
  join_date as join_date,
  count(order_id) as orders_in_2019
from Users u
left join Orders o
on  u.user_id = o.buyer_id 
and (o.order_date  >= '2019-01-01' and o.order_date  < '2020-01-01')
group by user_id, join_date