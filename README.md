# Web_Scraping

This Python script scrapes product information from eBay based on a search term and number of pages specified. It collects the title, price, and link of each product listed and stores the data in a CSV file.

## Features
- **Scrapes product information (title, price, link) from eBay.**
- **Saves the extracted data into a CSV file.**
- **Utilizes the requests library for sending HTTP requests.**
- **Uses BeautifulSoup from bs4 to parse the HTML of eBay search results.**
- **Adds a delay between page requests to avoid overwhelming the server.**

## Requirements
- **Python 3.x.**
- **Libraries: requests, beautifulsoup4, csv.**

## Notes
- **The script pauses for 2 seconds between requests to avoid overloading the eBay server.**
- **Make sure you are following eBay's terms of service when scraping data.**
