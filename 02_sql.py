# INSERT Command

# import sqlite3 library
import sqlite3

# create the conncection object
connection = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = connection.cursor()

try:
    # insert data
    cursor.execute("""
        INSERT INTO populations
        VALUES('New York City', 'NY', 8400000)
    """)
    cursor.execute("""
        INSERT INTO populations
        VALUES('San Francisco', 'CA', 800000)
    """)

    # commit the changes
    connection.commit()
except sqlite3.OperationalError as err:
    print("Oops!  Something went wrong. Try again...")
    print('Operational error:', err)

# close the database connection
connection.close()

# or rewritten with "with"
# with sqlite3.connect("new.db") as connection:
#   c = connection.cursor()
#   c.execute("""
#       INSERT INTO population
#       VALUES('New York City', 'NY', 8400000)
#   """)
#   c.execute("""
#       INSERT INTO population
#       VALUES('San Francisco', 'CA', 800000)
#   """)
#
