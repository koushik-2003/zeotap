import sqlite3
from datetime import datetime

def calculate_daily_summary():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    query = '''
    SELECT city, 
           MIN(temperature), 
           MAX(temperature), 
           AVG(temperature), 
           weather, 
           COUNT(*) as count 
    FROM weather_data 
    WHERE timestamp >= strftime('%s', 'now', 'start of day') 
    GROUP BY city 
    ORDER BY count DESC
    '''
    c.execute(query)
    daily_summary = c.fetchall()
    
    for summary in daily_summary:
        print(f"City: {summary[0]}, Min Temp: {summary[1]:.2f}, Max Temp: {summary[2]:.2f}, Avg Temp: {summary[3]:.2f}, Dominant Weather: {summary[4]}")

    conn.close()

if __name__ == "__main__":
    calculate_daily_summary()
def check_alerts():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    query = '''SELECT city, temperature FROM weather_data WHERE temperature > 35'''
    c.execute(query)
    alerts = c.fetchall()
    
    for alert in alerts:
        print(f"ALERT: {alert[0]} exceeds temperature threshold with {alert[1]:.2f}°C")
    
    conn.close()
