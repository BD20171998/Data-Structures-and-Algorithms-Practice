-- 1407. Top Travellers
--https://leetcode.com/problems/top-travellers/
select Users.name, 
sum(IFNULL(Rides.distance, 0)) as travelled_distance
from Users
left join Rides
on Rides.user_id = Users.id
group by Users.id
order by travelled_distance desc, Users.name
