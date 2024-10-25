import matplotlib.pyplot as plt
import sqlite3

def generate_visualizations():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    # Fetch average temperature for each city
    query = '''SELECT city, AVG(temperature) FROM weather_data GROUP BY city'''
    c.execute(query)
    data = c.fetchall()

    cities = [row[0] for row in data]
    avg_temps = [row[1] for row in data]

    # Bar chart of average temperatures
    plt.figure(figsize=(10, 6))
    plt.bar(cities, avg_temps, color='skyblue')
    plt.xlabel('Cities')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Average Temperatures of Indian Metros')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('avg_temperature.png')  # Save the visualization to a file
    plt.show()

    # Fetch maximum, minimum, and average temperature for each city
    query = '''SELECT city, MIN(temperature), MAX(temperature), AVG(temperature) FROM weather_data GROUP BY city'''
    c.execute(query)
    data = c.fetchall()

    cities = [row[0] for row in data]
    min_temps = [row[1] for row in data]
    max_temps = [row[2] for row in data]
    avg_temps = [row[3] for row in data]

    # Line chart for Min, Max, Avg temperatures
    plt.figure(figsize=(10, 6))
    plt.plot(cities, min_temps, label='Min Temp', color='blue', marker='o')
    plt.plot(cities, max_temps, label='Max Temp', color='red', marker='o')
    plt.plot(cities, avg_temps, label='Avg Temp', color='green', marker='o')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends for Indian Metros')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('temp_trends.png')  # Save the visualization to a file
    plt.show()

    conn.close()

if __name__ == "__main__":
    generate_visualizations()
