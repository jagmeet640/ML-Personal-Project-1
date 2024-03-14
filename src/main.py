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
templates = Jinja2Templates(directory="template")

# Define a route for the home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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






