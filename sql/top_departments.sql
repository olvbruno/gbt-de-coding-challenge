WITH department_hiring AS (
    SELECT
        d.id,
        d.department,
        COUNT(e.id) AS hired,
        AVG(COUNT(e.id)) OVER () AS avg_hired
    FROM
        employees e
    JOIN
        departments d ON e.department_id = d.id
    WHERE
        strftime('%Y', e.datetime) = '2021'
    GROUP BY
        d.id,
        d.department
)
SELECT
    id,
    department,
    hired
FROM
    department_hiring
WHERE
    hired > avg_hired
ORDER BY
    hired DESC;
