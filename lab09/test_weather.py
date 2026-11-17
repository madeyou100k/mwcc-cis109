# CIS109 - Lab 09
# Unit Tests for Weather Application

from unittest.mock import patch
from weather import get_coordinates, get_noaa_endpoint, get_noaa_forecast

# Test 1: Check latitude and longitude
@patch("weather.requests.get")
def test_get_coordinates(mock_get):

    # Create sample OpenStreetMap data
    mock_get.return_value.json.return_value = [
        {
            "lat": "18.2066971",
            "lon": "-65.9139804"
        }
    ]

    # Call the function
    lat, lon = get_coordinates("Juncos, PR")

    # Check that the coordinates match
    assert lat == "18.2066971"
    assert lon == "-65.9139804"


# Test 2: Check NOAA forecast URL
@patch("weather.requests.get")
def test_get_noaa_endpoint(mock_get):

    # Create sample NOAA endpoint data
    mock_get.return_value.json.return_value = {
        "properties": {
            "forecast": "https://api.weather.gov/gridpoints/SJU/178,109/forecast"
        }
    }

    # Call the function
    url = get_noaa_endpoint("18.2066971", "-65.9139804")

    # Check the returned forecast URL
    assert url == "https://api.weather.gov/gridpoints/SJU/178,109/forecast"


# Test 3: Check NOAA forecast periods
@patch("weather.requests.get")
def test_get_noaa_forecast(mock_get):

    # Create sample forecast data
    mock_get.return_value.json.return_value = {
        "properties": {
            "periods": [
                {
                    "name": "Today",
                    "temperature": 88,
                    "shortForecast": "Partly Sunny"
                },
                {
                    "name": "Tonight",
                    "temperature": 73,
                    "shortForecast": "Scattered Rain Showers"
                }
            ]
        }
    }

    # Call the function
    periods = get_noaa_forecast("https://example.com/forecast")

    # Check the forecast information
    assert len(periods) == 2
    assert periods[0]["temperature"] == 88
    assert periods[1]["name"] == "Tonight"