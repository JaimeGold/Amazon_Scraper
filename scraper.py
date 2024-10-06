from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv

# Path to your ChromeDriver (update this to the location on your machine)
chrome_driver_path = "C:/Drivers/chromedriver.exe"

# Set up the Selenium WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the Amazon best sellers page
url = "https://www.amazon.com/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm"
driver.get(url)
driver.maximize_window()

# Wait for the page to load
time.sleep(2)  # Adjust this delay if necessary

# Create an ActionChains object
actions = ActionChains(driver)

# Scroll down using the mouse wheel
scroll_attempts = 12  # Number of scroll attempts
for _ in range(scroll_attempts):
    # Scroll down by a certain amount
    actions.move_to_element(driver.find_element("tag name", "body")).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(0.5)  # Wait for new items to load

# Once all items are loaded, extract the page source
html = driver.page_source
driver.quit()  # Close the browser once scraping is done

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract items
items = soup.find_all("div", class_="zg-grid-general-faceout")

data = []

# Iterate over each item
for rank, item in enumerate(items, start=1):
    # Extract item name
    name_tag = item.find("div", class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
    name_alt = item.find("div", class_="_cDEzb_p13n-sc-css-line-clamp-4_2q2cc")
    name = name_tag.get_text(strip=True) if name_tag else (name_alt.get_text(strip=True) if name_alt else "No name")
    
    # Extract item link
    link_tag = item.find("a", class_="a-link-normal")
    link = f'https://www.amazon.com{link_tag["href"]}' if link_tag else "No link"
    
    # Extract item price
    price_tag = item.find("span", class_="_cDEzb_p13n-sc-price_3mJ9Z")
    price_alt = item.find("span", class_="p13n-sc-price")
    price = price_tag.get_text(strip=True)[1:] if price_tag else (price_alt.get_text(strip=True)[1:] if price_alt else "No price")
    # Extract review count
    review_count_tag = item.find("span", class_="a-size-small")
    review_count = review_count_tag.get_text(strip=True) if review_count_tag else "No reviews"
    # Extract rating (review value)
    rating_tag = item.find("span", class_="a-icon-alt")
    rating = rating_tag.get_text(strip=True)[:3] if rating_tag else "No rating"
    # Append the data to the list as a dictionary
    data.append({
        "Rank": rank,
        "Name": name,
        "Link": link,
        "Price": price,
        "Review Count": review_count,
        "Rating": rating
    })

# Define CSV file name
csv_file = "amazon_best_sellers.csv"
    
# Write the data to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Rank", "Name", "Link", "Price", "Review Count", "Rating"])
    writer.writeheader()
    writer.writerows(data)

print(f"Data successfully written to {csv_file}")
