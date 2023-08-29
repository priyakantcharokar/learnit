
# Replace 'YOUR_API_KEY' with your actual Google Maps API key, and provide the latitude and longitude coordinates for the origin and destination variables.
# INSTALL --> pip install -U googlemaps
# Please note that you'll need to sign up for a Google Cloud account and enable the Google Maps JavaScript API to obtain an API key. 
#   Also, make sure to review Google's terms of use for their APIs and billing details.

import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

def calculate_distance(origin, destination):
    # Get the distance matrix response
    distance_matrix = gmaps.distance_matrix(origin, destination, units='metric')

    # Extract distance in meters
    distance_in_meters = distance_matrix['rows'][0]['elements'][0]['distance']['value']

    return distance_in_meters

if __name__ == "__main__":
    origin = (latitude1, longitude1)  # Replace with your actual origin coordinates
    destination = (latitude2, longitude2)  # Replace with your actual destination coordinates

    distance = calculate_distance(origin, destination)

    print(f"Distance between the two points: {distance} meters")


