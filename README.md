# Amazon_Scraper
This project scrapes Amazon's best sellers in the kitchen category and extracts information such as product name, price, review count, and ratings. The scraped data is saved into a CSV file. This project uses **Selenium** to simulate scrolling and load all 50 best-selling items on the page.
## Table of Contents
- [Project Overview](#Project_Overview)
- [Features](#Features)
- [Requirements](#Requirements)
- [Setup Instructions](#Setup_Instructions)
- [Usage](#Usage)
- [Output](#Output)
- [Notes](#Notes)
## Project Overview
The script automates collecting product information from the Amazon Best Sellers page. Using Selenium, the script simulates scrolling to load all items. Once all items are loaded, the data is scraped using BeautifulSoup and saved in a CSV file.
## Features
- Scrapes top 50 best-selling kitchen products from Amazon.
- Extracts the following information for each product:
  - Rank
  - Product Name
  - Product Link
  - Price
  - Review Count
  - Rating
- Saves the data into a CSV file for easy analysis.
## Requirements
Before running the project, ensure you have the following dependencies installed:
- Python 3.8+
- Selenium
- BeautifulSoup4
- Requests
- Chrome WebDriver (Compatible with your version of Google Chrome)
You can install the Python dependencies using:
```bash
pip install -r requirements.txt
```
## Requirements File (`requirements.txt`)
```txt
beautifulsoup4
selenium
requests
```
## Setup Instructions
1. **Clone the repository**:
```bash
git clone https://github.com/your-username/amazon-scraper.git
cd amazon-scraper
```
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```
3. **Download Chrome WebDriver**:
- Download the appropriate version of [Chrome WebDriver](https://developer.chrome.com/docs/chromedriver/downloads) based on your Chrome version.
- Extract and add the file to the project directory or ensure it’s in your system's PATH.
4. **Set up WebDriver Path**:
Update the path to your `chromedriver` in the `scraper.py` file:
```python
chrome_driver_path = "/path/to/chromedriver"
```
## Usage
To run the scraper, execute the `scraper.py` script:
```bash
python scraper.py
```
### Example Output
After running the script, a CSV file named `amazon_best_sellers.csv` will be created with the following structure:

| Rank | Name           | Link                               | Price | Review Count | Rating |
| ---- | -------------- | ---------------------------------- | ----- | ------------ | ------ |
| 1    | Product Name 1 | https://www.amazon.com/dp/example1 | 25.99 | 1,234        |	4.7    |
| 2    | Product Name 2 | https://www.amazon.com/dp/example2 | 45.99 | 567	        | 4.5    |
| 3    | Product Name 3 | https://www.amazon.com/dp/example3 | 19.99 | 890	        | 4.3    |
## Output
- A CSV file named `amazon_best_sellers.csv` will be created in the project directory.
- The file contains the following columns:
  - Rank
  - Product Name
  - Product Link
  - Price
  - Review Count
  - Rating
## Notes
- **Rate Limiting**: Be cautious while scraping Amazon, as they may rate-limit or block your IP if requests are made too frequently. To handle this, the script includes random delays and retries to avoid hitting rate limits.
- **Dynamic Content**: Since Amazon dynamically loads content, we use Selenium to simulate scrolling and load all 50 items.
