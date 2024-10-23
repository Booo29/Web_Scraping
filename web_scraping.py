import requests
from bs4 import BeautifulSoup
import csv
import time

def get_ebay_products(search_term, num_pages):
    products = []

    for page in range(1, num_pages + 1):
        url = f'https://www.ebay.com/sch/i.html?_nkw={search_term}&_pgn={page}'
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error accessing the page {page}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')

        items = soup.find_all('li', class_='s-item')
     
        for item in items:
            title_element = item.find('span', role='heading')
            price_element = item.find('span', class_='s-item__price')
            link_element = item.find('a', class_='s-item__link')
           
            if title_element and price_element and link_element:
                title = title_element.text
                price = price_element.text
                link = link_element['href']

                products.append({
                    'title': title,
                    'price': price,
                    'link': link
                })

        time.sleep(2)

    return products

def save_to_csv(products, filename):
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'link'])
        writer.writeheader()
        writer.writerows(products)

def main():
    search_term = 'laptop'
    num_pages = 1 
    filename = 'ebay_products.csv' 

    products = get_ebay_products(search_term, num_pages)

    save_to_csv(products, filename)

    print(f"Information of {len(products)}  products stored in'{filename}'.")

if __name__ == '__main__':
    main()
