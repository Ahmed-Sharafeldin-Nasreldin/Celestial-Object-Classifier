import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download an image given its URL
def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded successfully: {save_path}")
    else:
        print(f"Error downloading image: {response.status_code}")

# URL of the APOD website
apod_url = 'https://apod.nasa.gov/apod/archivepix.html'

# Create a folder to store downloaded images
output_folder = 'apod_images'
os.makedirs(output_folder, exist_ok=True)

# Send a GET request to the APOD website and parse the HTML
response = requests.get(image_url, timeout=30)  # Adjust timeout value as needed

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all image links on the page
    image_links = soup.find_all('a', href=lambda href: href and href.endswith('.html'))
    
    # Iterate over image links and download images
    for link in image_links:
        image_page_url = urljoin(apod_url, link['href'])
        image_page_response = requests.get(image_page_url)
        if image_page_response.status_code == 200:
            image_soup = BeautifulSoup(image_page_response.content, 'html.parser')
            image_tag = image_soup.find('img')
            if image_tag:
                image_url = urljoin(apod_url, image_tag['src'])
                image_name = os.path.basename(image_url)
                save_path = os.path.join(output_folder, image_name)
                download_image(image_url, save_path)
        else:
            print(f"Error downloading image page: {image_page_response.status_code}")
else:
    print(f"Error retrieving APOD archive page: {response.status_code}")
