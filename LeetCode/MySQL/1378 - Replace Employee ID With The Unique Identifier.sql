-- 1378. Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

select
        unique_id,
        name  
    from
        Employees 
    left join
        EmployeeUNI 
            on Employees.id = EmployeeUNI.id