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

# Warm-up 1-10-2023
#-- Using the farmers market - Create a new column based off of cost_to_customer_per_qty.
#-- If the cost was less than or equal to 1 label them as Cheap
#-- If the cost was greater than 1 but less than 5 label them as Mid-range
#-- If the cost was greater than or equal to 5 label them as High-end


USE farmers_market;

SELECT *,
	CASE
       WHEN cost_to_customer_per_qty <= 1 THEN 'cheap'
       WHEN cost_to_customer_per_qty  <5 THEN 'mid-range'
       WHEN cost_to_customer_per_qty >=5 THEN 'high-end'
   END AS price_category
FROM customer_purchases
ORDER BY cost_to_customer_per_qty;


# Warm-up 1-18-2023
#--  What is the current average salary for each of the following department
#-- groups: R&D, Sales & Marketing, Prod & QM, Finance & HR, Customer Service?

USE employees;

SELECT 
	CASE
		When d.dept_name in ('Research', 'Development')Then 'R&D'
        When d.dept_name in ('Sales', 'Marketing')Then 'Sales 7 Marketing'
        When d.dept_name in ('Production', 'Quality Management')Then 'Prod % QM'
        When d.dept_name in ('Fincnace', 'Human Resources')Then 'Rfiance & HR'
        WHEN d.dept_name in ('Customer Service') Then 'CS'
	END AS dept_group, AVG(salary)
FROM departments as d
JOIN dept_emp de USING(dept_no)
JOIN salaries s USING(emp_no)
WHERE s.to_Date > NOW() and de.to_date > NOW()
GROUP By dept_group
