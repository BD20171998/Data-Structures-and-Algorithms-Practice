--595. Big Countries
--https://leetcode.com/problems/big-countries/

SELECT name, area, population
FROM World
WHERE area > 3000000 or population > 25000000