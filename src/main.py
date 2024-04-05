from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import toml 
import pymysql
from pydantic import BaseModel


config = toml.load('config/secret.toml')

myConnection = pymysql.connect(
    host= config['database']['host'],
            user= config['database']['username'],
            password= config['database']['password'],
            database= config['database']['database'],
            port= config['database']['port']
)

class Employee(BaseModel):
    EmpID: int
    name: str
    age: str
    number: int
    department: str
    post: str


# Initialize the FastAPI app
app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define a route for the home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/employeeEnter/")
def enterEmployee(emp: Employee):
    try:
        with myConnection.cursor() as cursor:
            sql_query = "INSERT INTO Employee (EmpID, Name, Age, Number, Department, Post) VALUES (%s, %s, %s, %s, %s, %s);"
            cursor.execute(sql_query, (emp.EmpID, emp.name, emp.age, emp.number, emp.department, emp.post))
            myConnection.commit()
            return emp
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error!!!")
    
@app.get("/employeeByName/{name}")
def getEmpByName(name: str):
    try: 
        with myConnection.cursor() as cursor:
            sql_query = "select * from Employee where name = %s"
            cursor.execute(sql_query, (name,))
            employeeByName = cursor.fetchall()

            if not employeeByName: 
                raise HTTPException(status_code=400, detail="Error empoloyee not found!!!")
            return employeeByName
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error!!!")
            
@app.delete("/deleteEmployee/{name}")
def deleteEmployee(name: str):
    try:
        with myConnection.cursor() as cursor:
            sql_query = 'delete from Employee where name = %s'
            cursor.execute(sql_query, (name,))
            myConnection.connect()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error In Deleting!!!")
    


@app.get("/employees/")
def GetAllEmployeeData():
    try:
        with myConnection.cursor() as cursor:
            sql_query = "SELECT * FROM Employee"
            cursor.execute(sql_query)
            employee_data = cursor.fetchall()
            # myConnection.commit()
            
            if not employee_data:
                raise HTTPException(status_code=404, detail="Employee data not found")
            return employee_data
    except Exception as e:
        raise HTTPException(status_code= 500, detail="internal server error")
    

@app.get("/empByPost/{post}")
def getAllEmployeePost(post: str):
    try: 
        with myConnection.cursor() as cursor:
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
        with myConnection.cursor() as cursor:
            sql_query = "select * from Employee where Department = %s"
            cursor.execute()
            employee_dept_data = cursor.fetchall()

            if not employee_dept_data:
                raise HTTPException(status_code=400, detail="Employee department datanot found!!!")
            return employee_dept_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server error!!!")
    
@app.get("/Salaries/")
def GetAllSalaries():
    try:
        with myConnection.cursor() as cursor:
            sql_query = "select Company.Employee.EmpID as Id, Company.Employee.name, Company.Employee.Department, Company.Employee.Post, Company.Salaries.HourlyWage * Company.Salaries.Hours_Per_month as Base,Company.Salaries.HourlyWage * 1.5 * Company.Salaries.OverTime_Hours_Per_month as Overtime,(Company.Salaries.HourlyWage * Company.Salaries.Hours_Per_month) + (Company.Salaries.HourlyWage * 1.5 * Company.Salaries.OverTime_Hours_Per_month) as Total from Company.Employee left join Company.Salaries on Company.Employee.EmpID = Company.Salaries.EmpID"

            cursor.execute(sql_query)

            salaries_data = cursor.fetchall()

            if not salaries_data:
                raise HTTPException(status_code=400, detail="Salaries empty")
        
            return salaries_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="internal server error")

    

