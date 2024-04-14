"""
import os

def create_directory():

    # Function to create directories 'json' and 'images' if they do not exist

    if not os.path.exists("assets/json/NASA"):
        os.makedirs("json/NASA")
        print("JSON directory created.")
    if not os.path.exists("img"):
        os.makedirs("assets/img/NASA")
        print("Images directory created.")
"""

import os

def create_directory():
    """
    Function to create directories 'json' and 'images' if they do not exist
    """
    json_path = "/assets/json/NASA"
    img_path = "/assets/img/NASA"
    if not os.path.exists(json_path):
        os.makedirs(json_path)
        print("JSON directory created.")
    if not os.path.exists(img_path):
        os.makedirs(img_path)
        print("Images directory created.")
