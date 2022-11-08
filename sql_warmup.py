Warm-up 11-9-2022
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
