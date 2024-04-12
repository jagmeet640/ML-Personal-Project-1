# backend.py (Flask application)

from flask import Flask, render_template, jsonify

import requests
from flask import Flask, render_template, request, redirect, url_for

import toml 
import pymysql
from pydantic import BaseModel
import requests




app = Flask(__name__)

# Define routes to serve HTML templates
@app.route('/')
def index():
    return render_template('index.html', url_for=url_for)


@app.route('/AddEmployeePage')
def get_addEmployeePage():
    return render_template('index_add_emp.html', url_for=url_for)


@app.route('/deleteEmployeePage')
def get_deleteEmployeePage():
    return render_template('index_delete_emp.html', url_for=url_for)

# Define routes to serve data through APIs
@app.route('/api/employees')
def get_employees():
    # Make a request to your FastAPI endpoint to fetch employee data
    response = requests.get('http://127.0.0.1:8000/employees/')
    return jsonify(response.json())


@app.route('/view')
def view():
    employee_data = requests.get('http://127.0.0.1:8000/employees/')
    employee_data = employee_data.json()
    return render_template('index_view.html', url_for= url_for, employee_data=employee_data)
    # return render_template('index_view.html', url_for=url_for)

@app.route('/testMysql')
def testMySql():
    employee_data = requests.get('http://127.0.0.1:8000/employees/')
    employee_data = employee_data.json()
    return employee_data


## Data base functionality routes :


@app.route('/addEmployees', methods=['POST', 'GET'])
def add_employee():
    # Get employee data from form
    employee_data = {
        'EmpID': request.form['EmpID'],
        'name': request.form['name'],
        'age': str(request.form['age']),
        'number': request.form['number'],
        'department': request.form['department'],
        'post': request.form['post']
    }
    # Send POST request to FastAPI endpoint to add employee
    response = requests.post('http://127.0.0.1:8000/employeeEnter/', json=employee_data)
    if response.status_code == 200:
        return redirect(url_for('view'))  # Redirect to view page if employee added successfully
    else:
        return "Failed to add employee"



# @app.route('/deleteEmployee', methods=['POST', 'GET'])
# def deleteEmployee():
#     employee_name = request.form['name']
#     requests.delete('http://127.0.0.1:8000/deleteEmployee/', employee_name)




# @app.route('/api/salaries')
# def get_salaries():
#     # Make a request to your FastAPI endpoint to fetch salary data
#     response = requests.get('http://127.0.0.1:8000/Salaries/')
#     return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
