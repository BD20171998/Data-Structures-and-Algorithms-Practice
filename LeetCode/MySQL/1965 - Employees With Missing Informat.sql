-- 1965. Employees With Missing Information
-- https://leetcode.com/problems/employees-with-missing-information/

select Salaries.employee_id from Employees
right join Salaries
on Employees.employee_id = Salaries.employee_id
where Employees.employee_id is NULL
union
select Employees.employee_id from Employees
left join Salaries
on Employees.employee_id = Salaries.employee_id
where Salaries.employee_id is NULL
order by employee_id asc