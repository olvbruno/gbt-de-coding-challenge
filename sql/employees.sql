-- Employees table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY, -- Id of the employee
    name TEXT NULL, -- Name and surname of the employee
    datetime TEXT NULL, -- Hire datetime in ISO format
    department_id INTEGER NULL, -- Id of the department which the employee was hired for
    job_id INTEGER NULL, -- Id of the job which the employee was hired for
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);

