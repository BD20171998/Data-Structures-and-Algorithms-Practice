-- 1148. Article Views I
-- https://leetcode.com/problems/article-views-i/

select distinct author_id as id 
from Views
where author_id = viewer_id
order by id asc