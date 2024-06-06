import os
import pytesseract
from PIL import Image
import re
import random
import mysql.connector


def ocr_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def generate_random_price():  # if the price is empty
    return random.randint(100, 199)


image_directory = 'restaurant_images'
processed_items = set()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="04022004",
    database="restaurant_menus"
)

mycursor = mydb.cursor()

for filename in os.listdir(image_directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        image_path = os.path.join(image_directory, filename)
        text = ocr_image(image_path)
        lines = text.split('\n')
        for line in lines:
            if not line.strip():
                continue
            prices = re.findall(r'\b\d+\b', line)
            if prices:
                name = re.sub(r'\b\d+\b.*', '', line)
                name = re.sub(r'[^a-zA-Z\s]', '', name)
                name = ' '.join(name.split())
                if len(name) > 2 and not any(char.isdigit() for char in name) and name not in processed_items:
                    price = int(prices[0])
                    if price == 0:
                        price = 100
                    elif price < 10:
                        price *= 100
                    elif 10 <= price <= 50:
                        price = generate_random_price()
                    price = min(price, 9999)
                    print(f"Item: {name}, Price: {price}")
                    sql = "INSERT INTO menu (item, price) VALUES (%s, %s)"
                    val = (name, str(price))
                    mycursor.execute(sql, val)
                    mydb.commit()
                    processed_items.add(name)
mydb.close()
