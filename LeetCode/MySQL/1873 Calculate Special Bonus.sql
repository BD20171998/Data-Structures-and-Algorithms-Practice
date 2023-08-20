-- #1873 Calculate Special Bonus
-- https://leetcode.com/problems/calculate-special-bonus/

select employee_id,
case 
when LEFT(name, 1) Not LIKE "M%" and mod(employee_id,2) <>0 then salary
else 0
end as "bonus"
from Employees
order by employee_id