SELECT
    d.department,
    j.job,
    SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '01' AND '03' THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '04' AND '06' THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '07' AND '09' THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '10' AND '12' THEN 1 ELSE 0 END) AS Q4
FROM
    employees e
JOIN
    departments d ON e.department_id = d.id
JOIN
    jobs j ON e.job_id = j.id
WHERE
    strftime('%Y', e.datetime) = '2021'
GROUP BY
    d.department,
    j.job
ORDER BY
    d.department,
    j.job;
