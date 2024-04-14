# fetch_nasa_image.py
import requests
import json
from create_directory import create_directory

def fetch_nasa_image(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        create_directory()
        
        if 'date' in data:
            with open(f"assets/json/NASA/{data['date']}.json", "w") as f:
                json.dump(data, f)
            print("Saved the response to JSON file.")
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None