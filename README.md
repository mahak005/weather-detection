# Python Weather Detection 🌦️ 

A simple, command line weather application built with Python that fetches real time weather information for any supported city using the OpenWeatherMap API.

## About the Project

The Python Weather App allows users to check current weather conditions by entering a city name. It retrieves weather data from the OpenWeatherMap API and displays important details in an easy to read format.

## Features

- Search weather by city name
- Display temperature in Celsius
- Show feels-like temperature
- Display humidity and wind speed
- Show weather conditions
- Handle invalid cities and API errors 

## Technologies Used

- Python 
- Requests
- python-dotenv 
- OpenWeatherMap API
- Git & GitHub 

## Project Structure

```text
weather-detection/
│
├── weather.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mahak005/weather-detection.git
cd weather-detection
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get an API Key

1. Create an account at [OpenWeatherMap](https://openweathermap.org/api).
2. Generate or copy your API key from your account.
3. Wait for the key to become active if necessary.

### 5. Configure Environment Variables

Create a `.env` file in the project root directory and add:

```env
WEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

**Security:** Never commit your `.env` file or expose your API key publicly.

### 6. Run the Application

```bash
python weather.py
```

Enter a city name when prompted to view its current weather information.

## Example Output

```text
Enter city name: Indore

--- Weather Report ---
City: Indore
Temperature: 33.6 °C
Feels Like: 34.07 °C
Humidity: 37 %
Condition: clear sky
Wind Speed: 2.39 m/s
```

*Example output only. Actual weather values change depending on the city and time of the request.*

## API Reference

This project uses the OpenWeatherMap Current Weather Data API.

**Endpoint:**

```text
https://api.openweathermap.org/data/2.5/weather
```

The application sends the city name, API key, and metric units as request parameters.

- [OpenWeatherMap API Documentation](https://openweathermap.org/current)

## Future Improvements

- Build a graphical interface using Tkinter or a web interface using Flask.
- Display weather icons and additional weather details.
- Add a multi day weather forecast.
- Improve input validation and error messages.
- Allow users to save their favorite cities.

## Author

**Mahak Soni**

- GitHub: [@mahak005](https://github.com/mahak005)

