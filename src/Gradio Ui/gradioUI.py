import pymysql
import gradio as gr
import toml

config = toml.load('secret.toml')
# Function to interact with MySQL database
def save_to_database(name, age, height, weight, address, email, phone_number):
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(
            host= config['database']['host'],
            user= config['database']['username'],
            password= config['database']['password'],
            database= config['database']['database'],
            port= config['database']['port']
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to insert data into the database
        sql_query = "INSERT INTO student_details (name, age, height, weight, address, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
       
        # Execute the SQL query with the provided parameters
        cursor.execute(sql_query, (name, age, height, weight, address, email, phone_number))

        # Commit changes to the database
        connection.commit()

        # Close cursor and connection
        cursor.close()
        connection.close()

        return "Data saved successfully to the database!"

    except Exception as e:
        return f"Error saving data to the database: {str(e)}"


iface = gr.Interface(fn=save_to_database,
                     inputs=["text", "number", "number", "number", "text", "text", "text"], 
                     outputs="text",
                     title="Student Info",
                     description="Enter the student details: ")

iface.launch()
