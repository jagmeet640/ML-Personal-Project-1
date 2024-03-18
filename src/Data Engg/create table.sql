CREATE TABLE IF NOT EXISTS Company.Employee (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Age INT,
    Number VARCHAR(20),
    Department VARCHAR(100),
    Post VARCHAR(100)
);