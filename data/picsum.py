# from login import TELEGRAPH_API_KEY
import requests
from telegraph import Telegraph
# telegraph = Telegraph(access_token = TELEGRAPH_API_KEY)
from datetime import  datetime


class Picsum:
    def __init__(self, token = None):
        self.telegraph = Telegraph(access_token = token)

    def load_data(self):
        pass
    
    def save_photo(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                respons = self.telegraph.upload_file(file)
            return f"https://telegra.ph/{respons[0]['src']}"
        except:
            return 'https://telegra.ph/file/62785ec3c606da79ad966.jpg'