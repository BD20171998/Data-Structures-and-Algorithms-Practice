-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

select #Transactions.visit_id, 
customer_id 
, count(customer_id) as count_no_trans
from Visits
left join Transactions
on Transactions.visit_id = Visits.visit_id
and Transactions.visit_id not in (select visit_id from Transactions)

where Visits.visit_id  not in (select visit_id from Transactions)
group by Visits.customer_id