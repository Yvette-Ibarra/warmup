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

# Warm-up 12-05-2022
# Write a query to find the unique last names with a 'q' but not 'qu'.

USE employees;

SELECT distinct(last_name)
FROM employees
Where last_name like'%Q%' and last_name not like '%Qu%'


# Warm-up 01-09-2023
#  Using the employees DB, give me the last name and count of employees that have a last name that starts with SH and ends with Z

USE employees;
SELECT last_name, COUNT(last_name) AS 'numbers_of_emp'
FROM employees
WHERE last_name LIKE 'sh%z'
GROUP BY last_name