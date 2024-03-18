select Company.Employee.EmpID as Id, 
Company.Employee.name, Company.Employee.Department, 
Company.Employee.Post, 
Company.Salaries.HourlyWage * Company.Salaries.Hours_Per_month as Base,
Company.Salaries.HourlyWage * 1.5 * Company.Salaries.OverTime_Hours_Per_month as Overtime,
(Company.Salaries.HourlyWage * Company.Salaries.Hours_Per_month) + (Company.Salaries.HourlyWage * 1.5 * Company.Salaries.OverTime_Hours_Per_month) as Total
from Company.Employee
left join Company.Salaries
on Company.Employee.EmpID = Company.Salaries.EmpID

