-- Data Science Skills
-- https://datalemur.com/questions/matching-skills

SELECT DISTINCT candidate_id
FROM candidates

WHERE
    candidate_id IN
    (
        SELECT DISTINCT candidate_id
        FROM candidates
        WHERE
            skill IN ('Python', 'Tableau', 'PostgreSQL')
        GROUP BY candidate_id
        HAVING count(candidate_id) = 3
    )


