--1890. The Latest Login in 2020
-- https://leetcode.com/problems/the-latest-login-in-2020/
select user_id, max(time_stamp) as last_stamp
from Logins
where time_stamp >= '2020-01-01' and time_stamp < '2021-01-01'
group by user_id 