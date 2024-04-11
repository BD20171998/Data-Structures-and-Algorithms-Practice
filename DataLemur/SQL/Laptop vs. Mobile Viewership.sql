-- Laptop vs. Mobile Viewership
-- https://datalemur.com/questions/laptop-mobile-viewership

SELECT


    count(CASE device_type WHEN 'laptop' THEN device_type END) AS laptop_views,
    count(CASE device_type
        WHEN 'tablet' THEN device_type
        WHEN 'phone' THEN device_type
    END)
    AS mobile_views
FROM viewership;