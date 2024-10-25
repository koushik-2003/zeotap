import sqlite3

# Initialize the SQLite database (if not already created)
def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    # Create the main table for storing weather data
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data
                 (city TEXT, timestamp INTEGER, temperature REAL, feels_like REAL, weather TEXT)''')
    
    # Create a table for storing daily weather summaries
    c.execute('''CREATE TABLE IF NOT EXISTS daily_weather_summary
                 (city TEXT, date TEXT, min_temp REAL, max_temp REAL, avg_temp REAL, dominant_weather TEXT)''')
    
    conn.commit()
    conn.close()

# Insert weather data into the database
def insert_weather_data(city, temperature, feels_like, weather, timestamp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('INSERT INTO weather_data (city, timestamp, temperature, feels_like, weather) VALUES (?, ?, ?, ?, ?)',
              (city, timestamp, temperature, feels_like, weather))
    conn.commit()
    conn.close()

# Fetch all weather data for a specific city
def fetch_weather_data(city):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('SELECT * FROM weather_data WHERE city = ?', (city,))
    data = c.fetchall()
    conn.close()
    return data

# Fetch weather data for a specific city from the current day
def fetch_daily_weather(city):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    query = '''SELECT * FROM weather_data 
               WHERE city = ? AND timestamp >= strftime('%s', 'now', 'start of day')'''
    c.execute(query, (city,))
    data = c.fetchall()
    conn.close()
    return data

# Fetch the daily weather summary for a city
def fetch_daily_summary(city):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('SELECT * FROM daily_weather_summary WHERE city = ?', (city,))
    data = c.fetchall()
    conn.close()
    return data

# Fetch dominant weather condition for a city in a given day
def fetch_dominant_weather(city):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    query = '''SELECT weather, COUNT(weather) as count 
               FROM weather_data 
               WHERE city = ? AND timestamp >= strftime('%s', 'now', 'start of day') 
               GROUP BY weather 
               ORDER BY count DESC 
               LIMIT 1'''
    c.execute(query, (city,))
    dominant_weather = c.fetchone()
    conn.close()
    return dominant_weather[0] if dominant_weather else None

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
