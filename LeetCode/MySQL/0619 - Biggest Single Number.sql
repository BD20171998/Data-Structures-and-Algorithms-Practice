--619. Biggest Single Number
--https://leetcode.com/problems/biggest-single-number/

select
max(t1.num) as num
from 

(select num
from MyNumbers
group by num
having count(num)<2) t1