--620. Not Boring Movies
-- https://leetcode.com/problems/not-boring-movies/
select * 
from Cinema
where mod(id, 2) != 0
and description 
not like '%boring%'
order by rating desc;