# 181. Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
SELECT * 
FROM Employee AS ee 
LEFT JOIN Employee AS mgr
     ON ee.id = mgr.Id