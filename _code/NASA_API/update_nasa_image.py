"""
from fetch_nasa_image import fetch_nasa_image
from display_image import display_image

def main():
    api_key_filepath = 'NASA_API_KEY.txt'
    with open(api_key_filepath, "r") as f:
        api_key = f.readline().strip()  # NASA API key
    image_data = fetch_nasa_image(api_key)  # Fetch image data from NASA API
    display_image(image_data)  # Display space image

if __name__ == "__main__":
    main()
"""

import os
from fetch_nasa_image import fetch_nasa_image
from display_image import display_image

def main():
    api_key = os.getenv('NASA_API_KEY')  # 환경 변수에서 NASA API key 읽기
    if not api_key:
        raise ValueError("API key not found. Please set the 'NASA_API_KEY' environment variable.")
    
    image_data = fetch_nasa_image(api_key)  # Fetch image data from NASA API
    display_image(image_data)  # Display space image

if __name__ == "__main__":
    main()