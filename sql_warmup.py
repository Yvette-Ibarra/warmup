# Warm-up 11-9-2022
#Find the average salary of employees and the standard deviation of employees salary

USE employees;

SELECT avg(salary)
FROM salaries
WHERE to_date > curdate();

SELECT stddev(salary)
FROM salaries
WHERE to_date > curdate();

# alternative

USE employees;

SELECT avg(salary), STD(salary)
FROM salaries
WHERE to_date > curdate();

# Warm-up 11-10-2022
# Find the average salary per departments of current employees. (Use employees data)

USE employees;
SELECT departments.dept_name, avg(salaries.salary)
FROM salaries
JOIN dept_emp USING(emp_no)
JOIN departments USING (dept_no)
WHERE dept_emp.to_date<curdate()
AND salaries.to_date < curdate()
GROUP BY departments.dept_name;


# Warm-up 11-22-2022
## Retrieve the salary of the second highest paid current employee

USE employees;

SELECT salary
FROM salaries
WHERE to_date > curdate()
ORDER BY salary DESC limit 1,1;