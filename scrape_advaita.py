import os
import json
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# URLs to scrape
urls = {
    "home": "https://www.advaita-iiitbh.in/",
    "events": "https://www.advaita-iiitbh.in/events",
    "register_hackfest": "https://unstop.com/hackathons/inter-college-hackathon-advaita-tecno-cultural-fest-international-institute-of-information-technology-iiit-bh-857179",
    "register_cybersec_battle": "https://unstop.com/hackathons/cybersec-battle-international-institute-of-information-technology-iiit-bhubaneswar-890695?lb=02mBqKH",
    "pronights": "https://www.advaita-iiitbh.in/#pronights",
}

# Set up Selenium WebDriver with Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def clean_text(text):
    # Function to clean the scraped text
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    text = text.strip()  # Remove leading and trailing whitespace
    return text

# Function to scrape data
def scrape_advaita():
    data = []

    # Scrape each page
    for key, url in urls.items():
        driver.get(url)
        time.sleep(5)  # Allow time for the page to load
        content_raw = driver.find_element(By.TAG_NAME, "body").text
        content = clean_text(content_raw)

        # Create a dictionary for each scraped page
        page_data = {
            "url": url,  # Store the scraped URL
            "page_content": content,  # Store the scraped content
            "key": key  # Store the page key for identification
        }

        data.append(page_data)  # Append the dictionary to the data list
        print(f"Scraped {key} content: {content[:100]}...")

    return data

# Scrape the data
scraped_data = scrape_advaita()

# Save the scraped data to a JSON file
with open('scraped_data.json', 'w') as json_file:
    json.dump(scraped_data, json_file, indent=4)

# Close the driver
driver.quit()