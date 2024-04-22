from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import toml 
import pymysql
from pydantic import BaseModel


config = toml.load('config/secret.toml')

class Salary(BaseModel):
    EmpID: int
    name: str
    JoinDate: str
    HourlyRate: float
    BaseSalary: float


class Employee(BaseModel):
    EmpID: int
    name: str
    age: str
    number: int
    department: str
    post: str

class WorkDetails(BaseModel):
    EmpID: int
    name: str
    month: str
    hoursWorked: int
    offDays: int
    leaveDays: int


# Initialize the FastAPI app
app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define a route for the home page
# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

@app.post("/employeeEnter/")
def enterEmployee(emp: Employee):
    try:

        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = "INSERT INTO Employee (EmpID, Name, Age, Number, Department, Post) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor.execute(sql_query, (emp.EmpID, emp.name, emp.age, emp.number, emp.department, emp.post))
                connection.commit()
                return emp
            
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error!!!")
    
@app.get("/employeeByName/{name}")
def getEmpByName(name: str):
    try: 
        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = "select * from Employee where name = %s"
                cursor.execute(sql_query, (name,))
                employeeByName = cursor.fetchall()

                if not employeeByName: 
                    raise HTTPException(status_code=400, detail="Error empoloyee not found!!!")
                return employeeByName
            
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error!!!")
            
@app.delete("/deleteEmployee/{empID}")
def deleteEmployee(empID: int):
    try:
        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                print("in delete")
                print(empID)
                sql_query = 'delete from Employee where EmpID = %s'
                cursor.execute(sql_query, (empID,))
                connection.commit()
        return {"message": "Student deleted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error In Deleting!!!")
    


@app.get("/employees/")
def GetAllEmployeeData():
    try:
        # Establish the connection to MySQL database
        with pymysql.connect(
            host=config['database']['host'],
            user=config['database']['username'],
            password=config['database']['password'],
            database=config['database']['database'],
            port=config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = "SELECT * FROM Employee"
                cursor.execute(sql_query)
                employee_data = cursor.fetchall()

                if not employee_data:
                    raise HTTPException(status_code=404, detail="Employee data not found")

                return employee_data

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/empByPost/{post}")
def getAllEmployeePost(post: str):
    try: 
        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = "select * from Employee where Post = %s"
                cursor.execute()
                employee_post_data = cursor.fetchall(sql_query, (post,))

                if not employee_post_data:
                    raise HTTPException(status_code=400, detail="Employees not found error!!!")
                return employee_post_data
            
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Internal error !!!")

@app.get("/empByRole/{dept}")
def getAllEmployeeDept(dept: str):
    try:
        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = "select * from Employee where Department = %s"
                cursor.execute()
                employee_dept_data = cursor.fetchall()

                if not employee_dept_data:
                    raise HTTPException(status_code=400, detail="Employee department datanot found!!!")
                return employee_dept_data
            
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server error!!!")
    
@app.get("/salary/")
def getSalaryInfo():
    try: 
        with pymysql.connect(
            host= config['database']['host'],
            user= config['database']['username'],
            password= config['database']['password'],
            database= config['database']['database'],
            port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = 'Select * from Salary'
                cursor.execute(sql_query)
                salary_data = cursor.fetchall()
                if not salary_data:
                    raise HTTPException(status_code=404, detail="Employee data not found")
                return salary_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error !!!")
    
@app.post("/addSalary/")
def addSalaryInfo(sal: Salary):
    try:

        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = "INSERT INTO Company.Salary (EmpID, Name, JoinDate, HourlyRate, BaseSalary) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(sql_query, (sal.EmpID, sal.name, sal.JoinDate, sal.HourlyRate, sal.BaseSalary))
                connection.commit()
                return sal
            
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error!!!")
    
@app.delete("/deleteSalary/{empID}")
def deleteSalary(empID: int):
    try:
        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                print("in delete")
                # print(empID)
                sql_query = 'delete from Salary where EmpID = %s'
                cursor.execute(sql_query, (empID,))
                connection.commit()
        return {"message": "Student deleted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error In Deleting!!!")
    

@app.get("/workDetails/")
def getWorkDetails():
    try: 
        with pymysql.connect(
            host= config['database']['host'],
            user= config['database']['username'],
            password= config['database']['password'],
            database= config['database']['database'],
            port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = 'Select * from Work'
                cursor.execute(sql_query)
                work_data = cursor.fetchall()
                if not work_data:
                    raise HTTPException(status_code=404, detail="Employee data not found")
                return work_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error !!!")
    
@app.post("/addWorkDetails/")
def addWorkDetails(workDetails: WorkDetails):
    try:

        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                sql_query = "INSERT INTO Work (EmpID, name, month, hoursWorked, offDays, leaveDays) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor.execute(sql_query, (workDetails.EmpID, workDetails.name, workDetails.month, workDetails.hoursWorked, workDetails.offDays, workDetails.leaveDays))
                connection.commit()
                return workDetails
            
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error!!!")
    

@app.delete("/deleteWorkDetails/{empID}")
def deleteWorkDetails(empID: int):
    try:
        with pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
        ) as connection:
            with connection.cursor() as cursor:
                print("in delete")
                print(empID)
                sql_query = 'delete from Work where EmpID = %s'
                cursor.execute(sql_query, (empID,))
                connection.commit()
        return {"message": "Employee Work Details Deleted Successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error In Deleting!!!")