--1741. Find Total Time Spent by Each Employee
--https://leetcode.com/problems/find-total-time-spent-by-each-employee/
elect event_day as day,
emp_id,
sum(out_time-in_time) as total_time
from Employees
group by event_day, emp_id