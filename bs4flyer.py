import os
import requests
from bs4 import BeautifulSoup

def nations_flyer():
    url = 'https://nationsfreshfoods.ca/vaughan_flyer.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    flyer_images = soup.find_all('img', {'style': 'width: 100%'})
    flyers = [image['src'] for image in flyer_images]

    base_url = 'https://nationsfreshfoods.ca/'
    for index, flyer in enumerate(flyers):
        flyer_url = base_url + flyer
        print(flyer_url)

        img_data = requests.get(flyer_url).content
        with open(f'flyer_{index}.jpg', 'wb') as handler:
            handler.write(img_data)

nations_flyer()
