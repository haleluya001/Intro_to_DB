import mysql.connector
from mysql.connector import errorcode

def create_database():
    """
    Connects to the MySQL server and creates the 'alx_book_store' database
    if it does not already exist.
    """
    try:
        # Establish a connection to the MySQL server
        # You may need to change the user, password, and host
        # based on your local MySQL configuration.
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='127.0.0.1'
        )
        cursor = cnx.cursor()

        # SQL query to create the database if it doesn't exist
        database_name = "alx_book_store"
        query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
        
        # Execute the query
        cursor.execute(query)
        
        # If no errors occurred, the database was created or already existed.
        # Since we cannot use SELECT or SHOW to check, we assume success.
        print(f"Database '{database_name}' created successfully!")
        
    except mysql.connector.Error as err:
        # Handle different types of MySQL errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            # Print a generic error message for any other connection issues
            print(f"Failed to connect to the database: {err}")
    finally:
        # Ensure the cursor and connection are closed to free up resources
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'cnx' in locals() and cnx is not None:
            cnx.close()
            print("Connection closed.")

# Call the function to run the script
if __name__ == "__main__":
    create_database()