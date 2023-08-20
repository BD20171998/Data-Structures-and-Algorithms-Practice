-- 1141. User Activity for the Past 30 Days I
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

select activity_date as day, count(distinct user_id) as active_users
from Activity
group by activity_date#,session_id
having count(user_id)>=1
and activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY)
and activity_date<= '2019-07-27';