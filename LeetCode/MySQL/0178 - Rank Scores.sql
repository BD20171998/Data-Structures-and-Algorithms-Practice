--178. Rank Scores
--https://leetcode.com/problems/rank-scores/
 select score,
 dense_rank() over( order by score desc) "rank"
 from Scores