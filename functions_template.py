import pymysql
import toml

config = toml.load('secrets.toml')

# document for the basic work flow of all the functions for the RDBMs

## Basic DB functions 

# Funtion1 ~ review employee data
def getAllEmpData():

    myConnection = pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
    )

    cursor = myConnection.cursor()

    sql_query = "SELECT * from employee"

    employee_info = cursor.execute(sql_query)

    myConnection.commit()

    cursor.close()
    myConnection.close()

    return employee_info

# Function2 ~ review employee data (filter by designation)

def getDesgEmpData(designation):

    myConnection = pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
    )

    cursor = myConnection.cursor()

    sql_query = "SELECT * from Employee where designation = %s"

    employee_info = cursor.execute(sql_query, designation)

    myConnection.commit()

    cursor.close()

    myConnection.close()

    return employee_info

# Fuction3 ~ review empoloyee data (filter by dept)

def getDeptEmpData(dept):

    myConnection = pymysql.connect(
        host= config['database']['host'],
        user= config['database']['username'],
        password= config['database']['password'],
        database= config['database']['database'],
        port= config['database']['port']
    )

    cursor = myConnection.cursor()

    sql_query = "SELECT * from Employee where department = %s"

    employee_info = cursor.execute(sql_query, dept)

    myConnection.commit()

    cursor.close()

    myConnection.close()

    return employee_info 
