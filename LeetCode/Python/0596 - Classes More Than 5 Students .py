--596. Classes More Than 5 Students
--https://leetcode.com/problems/classes-more-than-5-students/

select class
from Courses
group by class
having count(class) >= 5