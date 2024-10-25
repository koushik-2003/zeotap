# Zeotap Weather Monitoring

## Description
Zeotap Weather Monitoring is a Python-based application that collects and visualizes weather data for different cities. It uses SQLite for data storage and Matplotlib for data visualization. The application provides insights into average, minimum, and maximum temperatures over time.

## Features
- Collects weather data for various cities.
- Stores data in a SQLite database.
- Visualizes weather data using Matplotlib.
- Generates bar and line charts for temperature analysis.

## Prerequisites
Before running the application, make sure you have the following installed:
- Python 3.x
- pip (Python package manager)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/koushik-2003/zeotap.git
   cd zeotap
2.(Optional) Create a virtual environment:
   python -m venv env
3.Activate the virtual environment:
   on windows:
   .\env\Scripts\activate
4.Install the required packages:
  pip install -r requirements.txt
Usage
1.Data Collection: Run the data collection script to populate the SQLite database:
python collect_weather_data.py
2.Data Visualization: Run the visualization script to generate charts:
python visualization.py
3.The generated charts will be saved as PNG files in the project directory.
Contributing
Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details
Acknowledgments
Matplotlib for data visualization.
SQLite for data storage.

### How to Use the README
- Place the above content in a file named `README.md` in your repository root.
- Ensure to include any additional details specific to your project, such as a list of required libraries in a `requirements.txt` file.
- Update any scripts mentioned in the instructions (like `collect_weather_data.py` and `visualization.py`) to match the actual script names in your project if they differ.

Feel free to customize any sections based on the specifics of your project!


