import mysql.connector
from datetime import datetime

# Connect to MySQL database
db = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Function to insert sensor readings into the database
def insert_reading(sensor_id, timestamp, value):
    sql = "INSERT INTO Reading (sensor_id, timestamp, value) VALUES (%s, %s, %s)"
    val = (sensor_id, timestamp, value)
    cursor.execute(sql, val)
    db.commit()
    print("Reading inserted successfully.")

# Example usage:
sensor_id = 1  # Assuming sensor ID 1 is attached to the solar panel
timestamp = datetime.now()  # Current timestamp
value = 25.5  # Example sensor reading value

# Insert the reading into the database
insert_reading(sensor_id, timestamp, value)

# Close the cursor and database connection
cursor.close()
db.close()
