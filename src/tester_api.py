import requests

# Testing if the item has been added works
# data = {
#     "EmpID": "0012",
#     "name": "John Doe",
#     "age": 30,
#     "number": "1234567890",
#     "department": "IT",
#     "post": "Developer"
# }

# # Make a POST request to the endpoint
# response = requests.post("http://127.0.0.1:8000/employeeEnter/", json=data)



response = requests.get("http://127.0.0.1:8000/employees/")
print(response)
