--610. Triangle Judgement
--https://leetcode.com/problems/triangle-judgement/

select x,y,z,

case 
    when x < z and y < z and x+y > z then "Yes"
    when x < y and z < y and x+z > y then "Yes"
    when y < x and z < x and y+z > x then "Yes"
    when x = y and x+y > z  then "Yes"
    when x = z and x+z > y  then "Yes"
    when y = z and y+z > x  then "Yes"
    else "No" 
    end as triangle

from Triangle