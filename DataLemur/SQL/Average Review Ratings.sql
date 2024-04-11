-- Average Review Ratings
-- https://datalemur.com/questions/sql-avg-review-ratings

SELECT

    product_id AS product,
    extract(MONTH FROM submit_date) AS mth,
    round(avg(stars), 2) AS avg_stars

FROM reviews

GROUP BY mth, product_id
ORDER BY mth, product_id;




