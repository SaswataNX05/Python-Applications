# Weather CLI Application

A command-line weather application that fetches real-time weather forecasts for any city worldwide using the free [Open-Meteo API](https://open-meteo.com/).

## Features

- Geocoding city name search to coordinates (latitude, longitude, country).
- Real-time temperature, apparent ("feels like") temperature, humidity, wind speed, and WMO weather condition code with weather emojis.
- Error handling for network drops, timeouts, and invalid cities.

## Requirements

Install dependencies using the root `requirements.txt`:
```bash
pip install -r requirements.txt
```
*(Or install `requests` directly: `pip install requests`)*

## How to Run

```bash
python weather_cli/main.py
```
Enter any city name when prompted (e.g. `Kolkata`, `London`, `Tokyo`).
