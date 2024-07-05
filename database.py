import psycopg2
from psycopg2 import sql
# Database connection parameters
DB_NAME = "your_database_name"
DB_USER = "your_username"
DB_HOST = "your_host"
DB_PORT = "your_port"
auth = authy1gWJ0mGgMXWGInJ6Vxf1cCPrXUw1CC77R8P7n3u
try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    # Create a cursor object
    cursor = connection.cursor()
    # Execute a SQL query to read data
    query = sql.SQL("SELECT * FROM {table}").format(table=sql.Identifier('your_table_name'))
    cursor.execute(query)
    # Fetch all rows from the executed query
    records = cursor.fetchall()
    # Print the fetched records
    for record in records:
        print(record)
except Exception as error:
    print("Error while connecting to PostgreSQL:", error)
finally:
    # Close the cursor and connection to the database
    if cursor:
        cursor.close()
    if connection:
        connection.close()
