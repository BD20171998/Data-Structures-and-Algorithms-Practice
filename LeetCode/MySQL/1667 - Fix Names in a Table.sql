-- #1667 Fix Names in a Table
-- https://leetcode.com/problems/fix-names-in-a-table/

select user_id,

concat(Upper(substring(name, 1,1)),lower(substring(name, 2))) as name
from Users
order by user_id
