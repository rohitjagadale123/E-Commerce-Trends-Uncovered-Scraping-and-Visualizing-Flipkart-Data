import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# URL of the Flipkart page to scrape
url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mobiles'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product containers
product_containers = soup.find_all('div', class_='_1AtVbE')

# Lists to store data
product_names = []
product_prices = []

# Loop through the product containers
for container in product_containers:
    # Extract product name
    product_name_element = container.find('div', class_='_4rR01T')
    if product_name_element:
        product_name = product_name_element.text
        product_names.append(product_name)
    
    # Extract product price
    product_price_element = container.find('div', class_='_30jeq3 _1_WHN1')
    if product_price_element:
        product_price = product_price_element.text
        product_prices.append(product_price)

# Data visualization
plt.figure(figsize=(10, 6))
plt.barh(product_names[:10], product_prices[:10], color='skyblue')
plt.xlabel('Price')
plt.ylabel('Product Name')
plt.title('Top 10 Mobile Phones on Flipkart')
plt.gca().invert_yaxis()  # Invert y-axis to display the highest price at the top
plt.tight_layout()

# Display the plot
plt.show()
