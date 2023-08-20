--570. Managers with at Least 5 Direct Reports
--https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

with ct as (

select managerId#, count(department) over(partition by department)
from Employee
group by managerId
having count(managerId)   > 4 
)

select name
from  Employee
where id in  (table ct)