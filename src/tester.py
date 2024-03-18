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
