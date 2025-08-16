import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user/password/host as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # replace with your MySQL username
            password="your_password"   # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database (IF NOT EXISTS prevents failure if already created)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error: Could not connect to the MySQL server. {e}")

    finally:
        # Ensure connection is closed
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            # Optional confirmation
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()