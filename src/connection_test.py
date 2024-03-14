import pymysql
import toml

config = toml.load('secret.toml')

def test_connection():
    try:
        # Establish a connection to the database
        connection = pymysql.connect(
            host= config['database']['host'],
            user= config['database']['username'],
            password= config['database']['password'],
            database= config['database']['database'],
            port= config['database']['port']
        )
        
        # If connection is successful, print a success message
        print("Connection successful!")
        
        # Close the connection
        connection.close()
        
    except Exception as e:
        # If connection fails, print the error message
        print("Connection failed:", str(e))

# Call the test_connection function to test the connection
test_connection()