# CIS109 - Lab 09
# Weather Averages

import argparse
import requests

# Get latitude and longitude from OpenStreetMap
def get_coordinates(city):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "MWCC"
    }

    response = requests.get(url, params=params, headers=headers, timeout=15)
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError("Location not found.")

    lat = data[0]["lat"]
    lon = data[0]["lon"]

    return lat, lon

# Get NOAA forecast endpoint using coordinates
def get_noaa_endpoint(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"

    headers = {
        "User-Agent": "MWCC"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    data = response.json()

    return data["properties"]["forecast"]

# Get weather forecast from NOAA
def get_noaa_forecast(url):
    headers = {
        "User-Agent": "MWCC"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    data = response.json()

    return data["properties"]["periods"]

# Main function for the weather application
def main():

    # Create command-line arguments
    parser = argparse.ArgumentParser(
        description="NOAA Weather Forecast Application"
    )

    # Required location argument
    parser.add_argument(
        "-l", "--location",
        required=True,
        help="Enter city and state, for example: Juncos, PR"
    )

    # Optional forecast arguments
    parser.add_argument(
        "-d", "--detailed",
        action="store_true",
        help="Display detailed forecast"
    )

    parser.add_argument(
        "-w", "--week",
        action="store_true",
        help="Display weekly forecast"
    )

    parser.add_argument(
        "-a", "--average",
        action="store_true",
        help="Display average temperature"
    )

    args = parser.parse_args()

    try:
        # Get coordinates from location
        lat, lon = get_coordinates(args.location)

        # Get NOAA endpoint
        forecast_url = get_noaa_endpoint(lat, lon)

        # Get forecast periods
        periods = get_noaa_forecast(forecast_url)

        if not periods:
            print("No forecast data available.")
            return

        print("\n================================")
        print("       NOAA WEATHER APP")
        print("================================")
        print(f"Location: {args.location}")
        print("--------------------------------")

        # Detailed forecast
        if args.detailed:
            current = periods[0]

            print(f"Period: {current['name']}")
            print(f"Temperature: {current['temperature']}°{current['temperatureUnit']}")
            print(f"Forecast: {current['detailedForecast']}")

        # Weekly forecast
        elif args.week:
            for period in periods:
                print(f"\n{period['name']}")
                print(f"Temperature: {current['temperature']}°{current['temperatureUnit']}")
                print(f"Forecast: {period['shortForecast']}")

        # Average temperature
        elif args.average:
            temperatures = []

            for period in periods:
                temperatures.append(period["temperature"])

            average = sum(temperatures) / len(temperatures)

            print(f"Average Temperature: {average:.1f}°F")

        # Default short forecast
        else:
            current = periods[0]

            print(f"Period: {current['name']}")
            print(f"Temperature: {current['temperature']}°F")
            print(f"Forecast: {current['shortForecast']}")

        print("================================\n")

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        print(f"Error retrieving weather data: {error}")

# Run the application
if __name__ == "__main__":
    main()