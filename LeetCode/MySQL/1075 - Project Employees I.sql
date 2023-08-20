--1075. Project Employees I
--https://leetcode.com/problems/project-employees-i/
select Project.project_id, 
round(sum(Employee.experience_years)/count(Project.project_id), 2) as average_years
from Project
inner join Employee
on Project.employee_id = Employee.employee_id
group by Project.project_id