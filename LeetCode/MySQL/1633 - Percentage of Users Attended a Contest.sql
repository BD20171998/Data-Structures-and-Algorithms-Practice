-- 1633. Percentage of Users Attended a Contest
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/

select
        Register.contest_id,
        case  
            when count(Register.contest_id) = 0 then 0 
            else round(100*(count(Register.contest_id)/(select
                count(user_id) 
            from
                Users)),
            2)  
        end as percentage   
    from
        Register 
    left join
        Users 
            on Users.user_id = Register.user_id 
    group by
        contest_id 
    order by
        percentage desc,
        contest_id asc