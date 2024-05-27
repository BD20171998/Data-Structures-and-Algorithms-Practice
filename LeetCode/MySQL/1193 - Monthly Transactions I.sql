-- 1193. Monthly Transactions I 
-- https://leetcode.com/problems/monthly-transactions-i/description/

select
    country,
    DATE_FORMAT(trans_date, '%Y-%m') as month,
    COUNT(COALESCE (country, 1)) as trans_count,
    COALESCE(SUM(case when state = 'approved' then amount end), 0)
        as approved_total_amount,
    COALESCE(COUNT(case when state = 'approved' then state end), 1)
        as approved_count,
    COALESCE(SUM(amount), 0) as trans_total_amount


from transactions
group by country, DATE_FORMAT(trans_date, '%Y-%m')