import json
import requests

API_TOKEN = 'your_api_token'
API_URL = 'https://api.digitalocean.com/v2/'
API_URL_DAILY_QUOTE = 'http://quotes.rest/qod.json'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(API_TOKEN)}

def get_account_info():

    api_url = '{0}account'.format(API_URL)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None