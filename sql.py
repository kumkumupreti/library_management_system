import pymysql

# Replace these values with your actual database connection details
host = "localhost"
user = "root"
password = "12345678"
database = "your_database_name"

try:
    # Create a connection object
    con = pymysql.connect(host=host, user=user, password=password, database=database)

    # Now you can perform operations using the connection

    # For example, you can create a cursor and execute a query
    with con.cursor() as cursor:
        cursor.execute("SELECT * FROM your_table")
        result = cursor.fetchall()
        print(result)

except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection in the finally block to ensure it gets closed even if an exception occurs
    if con:
        con.close()
