-- 176. Second Highest Salary
-- https://leetcode.com/problems/second-highest-salary/

ith my_cte as(
select *, ROW_NUMBER() OVER(ORDER BY salary desc) as rn
from Employee)

select 
ifnull((select  my_cte.salary from my_cte where my_cte.rn = 2),NULL) as SecondHighestSalary