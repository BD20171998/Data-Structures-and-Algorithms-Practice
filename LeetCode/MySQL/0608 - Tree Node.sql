-- 608. Tree Node
-- https://leetcode.com/problems/tree-node/

select id,
case
    when p_id is Null then "Root"
    when id in (select p_id from Tree ) and p_id is not NULL then "Inner"
    when id  in (select p_id from Tree) is null then "Leaf"
    end as type
    
from Tree