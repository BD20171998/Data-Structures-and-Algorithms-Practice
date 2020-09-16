#0196. Delete Duplicate Emails
#https://leetcode.com/problems/delete-duplicate-emails/

DELETE t1 FROM Person t1 
INNER JOIN Person t2
WHERE t1.Id > t2.Id AND t1.email = t2.email