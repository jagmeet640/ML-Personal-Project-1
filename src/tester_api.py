import requests

# testing the api for adding employees
# data = {
#     "EmpID": "0012",
#     "name": "John Doe",
#     "age": "30",  # Convert age to a string
#     "number": "1234567890",
#     "department": "IT",
#     "post": "Developer"
# }

# # Make a POST request to the endpoint
# response = requests.post("http://127.0.0.1:8000/employeeEnter/", json=data)

# # Print the response
# print(response.json())

# testing for deleting employees
# response = requests.delete("http://127.0.0.1:8000/deleteEmployee/12")
# print(response.json())

# # testing the api for viewing employees
# response = requests.get("http://127.0.0.1:8000/employees/")
# print(response.json())


# Testing the salary view endpoint
# # testing the api for viewing employees
response = requests.get("http://127.0.0.1:8000/salary/")
print(response.json())
