import requests
import os
import webbrowser

base_url = 'https://randomuser.me/api'

query_parameter = {'nat': 'ir',
                   'gender': 'female'}

response = requests.get(base_url, query_parameter)
print(response)
print(response.reason)
print(response.json())


# https://api.nasa.gov/

# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos
# ?earth_date=2015-6-3&api_key=DEMO_KEY
nasa_api_base_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
nasa_query = {
    'earth_date': '2022-08-29',
    'api_key': 'DEMO_KEY'
}

nasa_response = requests.get(nasa_api_base_url, nasa_query)
print(nasa_response)
# print((nasa_response.json()))
webbrowser.open(nasa_response.json().get('photos')[0]['img_src'])











