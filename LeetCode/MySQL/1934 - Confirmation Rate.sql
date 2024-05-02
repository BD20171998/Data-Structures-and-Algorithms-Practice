-- 1934. Confirmation Rate
-- https://leetcode.com/problems/confirmation-rate/description/

with tot_counts as (  select
        Signups.user_id,
        count(Confirmations.user_id) as total  
    from
        Signups  
    left join
        Confirmations  
            on Signups.user_id=Confirmations.user_id    
    group by
        Signups.user_id),   confirm_counts as (      select
        Signups.user_id,
        count(Confirmations.user_id) as confirmed  
    from
        Signups  
    left join
        Confirmations  
            on Signups.user_id=Confirmations.user_id  
    where
        Confirmations.action="confirmed"  
    group by
        Signups.user_id  )   select
        tot_counts.user_id,
        case   
            when tot_counts.total = 0 
            or confirm_counts.confirmed is null then 0    
            else  round(confirm_counts.confirmed/tot_counts.total,
            2)    
        end as confirmation_rate  
    from
        tot_counts  
    left join
        confirm_counts  
            on confirm_counts.user_id = tot_counts.user_id