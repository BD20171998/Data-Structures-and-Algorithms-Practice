
#184. Department Highest Salary
#https://leetcode.com/problems/department-highest-salary/

with cte as(

select Department.name as Department, 
Employee.name as Employee, 
Employee.salary as Salary,
rank() over(partition by Department.name order by Employee.salary desc) as rnk
from Employee
inner join Department
on Department.id = Employee.departmentId
)


select Department, 
Employee, 
Salary 
from cte 
where rnk=1 