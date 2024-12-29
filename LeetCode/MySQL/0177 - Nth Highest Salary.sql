-- 177. Nth Highest Salary
-- https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

  RETURN (

    select min(r.sal)
    from  (select salary as sal,
    dense_rank() over(order by salary desc) as rk 
    from Employee) r
    where r.rk = N

  );
END