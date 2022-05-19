--197. Rising Temperature
--https://leetcode.com/problems/rising-temperature/

select * #b.id#,a.recordDate
from Weather as a

left join Weather as b 
on a.recordDate = DATE_SUB(b.recordDate, INTERVAL 1 DAY)

where a.temperature<b.temperature
