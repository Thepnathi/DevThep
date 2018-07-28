import json
import requests

API_URL = 'https://talaikis.com/api/quotes/random/'

response = requests.get(API_URL)
data = response.json()

def get_random_quote():

    if response.status_code == 200:
        return data
    else:
        return None

