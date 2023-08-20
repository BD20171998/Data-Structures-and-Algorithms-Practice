--597. Friend Requests I: Overall Acceptance Rate
--https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/



with ta as(
select 
count(distinct requester_id, accepter_id) as tot_accepted

from
RequestAccepted),

tr as(
    select 
    count(distinct sender_id, send_to_id) as tot_requests
from FriendRequest
)

select 
round(
ifnull(
    
    (ifnull(ta.tot_accepted,0)/tr.tot_requests),0),2) as accept_rate 
from ta, tr