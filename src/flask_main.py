# backend.py (Flask application)

from flask import Flask, render_template, jsonify

import requests

app = Flask(__name__)

# Define routes to serve HTML templates
@app.route('/')
def index():
    return render_template('index2.html')

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
    return render_template('index_view.html', employee_data=employee_data)

@app.route('/api/salaries')
def get_salaries():
    # Make a request to your FastAPI endpoint to fetch salary data
    response = requests.get('http://127.0.0.1:8000/Salaries/')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
