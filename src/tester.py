import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

# API call
response = requests.get("http://127.0.0.1:8000/employees/")
data = response.json()

# Convert API response into a pandas DataFrame
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age', 'Phone', 'Department', 'Role'])

# Display DataFrame
print("DataFrame:")
print(df)

salaries = requests.get("http://127.0.0.1:8000/Salaries/")
sals = salaries.json()
print(sals)

df_sals = pd.DataFrame(sals, columns=['ID', 'Name', 'Department', 'Role', 'Base', 'Overtime', 'Total'])
print(df_sals)

