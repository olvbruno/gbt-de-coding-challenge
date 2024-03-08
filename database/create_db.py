import sqlite3
import os


def create_database(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # List of SQL files to be executed
    sql_files = ["sql/departments.sql", "sql/jobs.sql", "sql/employees.sql"]

    try:
        # Iterate over SQL files and execute queries
        for file in sql_files:
            with open(file, "r") as f:
                sql_query = f.read()
                cursor.execute(sql_query)
                conn.commit()
            print(f"Table created successfully: {file}")

    except Exception as e:
        print(f"Error creating tables: {e}")

    finally:
        # Close the connection to the database
        cursor.close()
        conn.close()

# Define the path to the database file
database_file = "database.db"

# Check if the database file already exists and remove it if it does
if os.path.exists(database_file):
    os.remove(database_file)
    print(f"Existing database file removed: {database_file}")

# Create the database and tables
create_database(database_file)
