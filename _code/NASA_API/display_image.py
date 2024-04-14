# display_image.py
import requests
from create_directory import create_directory

def display_image(data):
    if 'url' in data and 'date' in data:
        image_url = data['url']
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            image_data = response.content
            
            create_directory()
            with open(f"assets/img/NASA/{data['date']}_nasa_image.jpg", "wb") as f:
                f.write(image_data)
            print("Saved the NASA image.")
        except Exception as e:
            print(f"An error occurred when fetching the image: {e}")
    else:
        print("No image URL or date found in data.")
