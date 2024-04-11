-- Pharmacy Analytics (Part 1)
-- https://datalemur.com/questions/top-profitable-drugs

SELECT
    drug,
    round((total_sales - cogs), 2) AS total_profit
FROM pharmacy_sales
ORDER BY total_profit DESC
LIMIT 3