#Use the weather API and programmatically parse the API data and store it in a
database.
import requests
import mysql.connector
from datetime import datetime

# OpenWeatherMap API details
API_KEY = "your_openweathermap_api_key"
CITY_NAME = "your_city_name"
BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"

# Connect to MySQL database
db = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Function to fetch weather data from API and insert into database
def fetch_and_store_weather():
    response = requests.get(BASE_URL)
    data = response.json()

    # Extract relevant weather information
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    timestamp = datetime.fromtimestamp(data['dt'])

    # Insert weather data into database
    sql = "INSERT INTO Weather (description, temperature, humidity, wind_speed, timestamp) VALUES (%s, %s, %s, %s, %s)"
    val = (weather_description, temperature, humidity, wind_speed, timestamp)
    cursor.execute(sql, val)
    db.commit()
    print("Weather data inserted successfully.")

# Call the function to fetch and store weather data
fetch_and_store_weather()

# Close the cursor and database connection
cursor.close()
db.close()
