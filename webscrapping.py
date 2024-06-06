import requests
import os
from bs4 import BeautifulSoup

# List of restaurant URLs
restaurant_urls = [
    'https://www.eazydiner.com/mumbai/sodabottleopenerwala-bandra-kurla-complex-230953/menu',
    'https://www.eazydiner.com/mumbai/cafe-noir-lower-parel-south-mumbai-674423/menu',
    'https://www.eazydiner.com/mumbai/o22-trident-bandra-kurla-complex-bkc-223173/menu',
    'https://www.eazydiner.com/mumbai/surbhi-kandivali-east-230018/menu',
    'https://www.eazydiner.com/mumbai/tipsy-bro-rooftop-lounge-bar-luxury-dining-vashi-navi-mumbai-693134/menu'
]

max_images_per_restaurant = 4

if not os.path.exists('restaurant_images'):
    os.makedirs('restaurant_images')


def scrape_images(restaurant_url):
    response = requests.get(restaurant_url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    image_tags = soup.find_all('img', alt='', src=True)

    restaurant_name = restaurant_url.split('/')[-2]
    image_count = 0
    for img_tag in image_tags:
        if image_count >= max_images_per_restaurant:
            break
        img_url = img_tag['src']

        if img_url.startswith('data:image'):
            continue
        filename = f"{restaurant_name}_{image_count+1}.jpg"
        image_response = requests.get(img_url, stream=True)
        with open(f'restaurant_images/{filename}', 'wb') as out_file:
            out_file.write(image_response.content)
        image_response.close()
        print(
            f"Image '{filename}' downloaded successfully from {restaurant_url}.")
        image_count += 1


for restaurant_url in restaurant_urls:
    scrape_images(restaurant_url)

print("All images downloaded successfully.")
