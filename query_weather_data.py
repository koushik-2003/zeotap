import sqlite3

# Connect to the database
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Query all the weather data
c.execute('SELECT * FROM weather_data')

# Fetch all results
rows = c.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the connection
conn.close()
