#!/usr/bin/python3
import MySQLdb
import sys

# Check if all required arguments are provided
if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

# Retrieve command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# print("Connecting to MySQL with user={}, password={}, database={}"
# .format(username, password, database))

# Connect to MySQL
db = MySQLdb.connect(host="localhost", user=username,
                     passwd=password, db=database)


# Further logic to execute queries can be added here
cursor = db.cursor()

# Example query to fetch and print all states
cursor.execute("SELECT * FROM states ORDER BY id")
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()

