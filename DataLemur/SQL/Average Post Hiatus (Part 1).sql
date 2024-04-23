-- Average Post Hiatus (Part 1) 
-- https://datalemur.com/questions/sql-average-post-hiatus-1

select
    user_id,
    extract(
        day from max(post_date)
        - min(post_date)
    ) as days_between
from posts
where extract(year from post_date) = 2021
group by user_id

having count(user_id) > 1