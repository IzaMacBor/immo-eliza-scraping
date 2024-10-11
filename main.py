import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get HTML content from a URL
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

# Function to scrape property details from HTML
    
def property_details(html):
    soup = BeautifulSoup(html, 'html.parser')
    s = BeautifulSoup(features="lxml")
    details = {}

    property_id_element = soup.find('div', class_="classified__header--immoweb-code")
    details['Immoweb Code'] = property_id_element.text.strip() if property_id_element else None

    locality_element = soup.find("div", class_="classified__information--address", attrs={"aria-hidden": "true"})
    details['Locality'] = locality_element.get_text(strip=True) if locality_element else None

    postal_code_element = soup.find('span', class_="classified__information--address-row")
    details['Postal code'] = postal_code_element.text.strip() if postal_code_element else None

    price_element = s.find('span', class_="sr-only")
    details['Price'] = price_element.text.strip() if price_element else None

    type_of_property_element = soup.find()
    details['Type of property'] = type_of_property_element.text.strip() if type_of_property_element None
    
    subtype_of_property_element = soup.find()
    details['Subtype of property'] = subtype_of_property_element.text.strip() if subtype_of_property_element None

    type_of_sale_element = soup.find()
    details['Type of sale'] = type_of_sale_element.text.strip() if type_of_sale_element else None

    rooms_number_element = soup.find('span', class_="overview__text")
    details['Number of rooms'] = rooms_number_element.text.strip() if rooms_number_element else None

    living_area_element = soup.find('p', class_="classified__information", attrs={"aria-hidden": "true"})
    details['Living area'] = living_area_element.text.strip() if living_area_element else None

    kitchen_element = soup.find('tr', class_="classified-table__row")
    details['Equipped kitchen'] = kitchen_element.text.strip() if kitchen_element else None

    furnished_element = soup.find()
    details['Furnished'] = furnished_element.text.strip() if furnished_element else None

    open_fire_element = soup.find()
    details['Open fire'] = open_fire_element.text.strip() if open_fire_element else None

    terrace_element = soup.find()
    details['Terrace'] = terrace_element.text.strip() if terrace_element else None

    garden_element = soup.find()
    details['Garden'] = garden_element.text.strip() if garden_element else None

    facades_element = soup.find()
    details['Number of facades'] = facades_element.text.strip() if facades_element else None

    swimming_pool_element = soup.find()
    details['Swimming pool'] = swimming_pool_element.text.strip() if swimming_pool_element else None

    state_element = soup.find()
    details['State of building'] = state_element.text.strip() if state_element else None
    

    return details

# Load URLs from the CSV file
url_file_path = r"C:\Users\izama\Desktop\repo\immo-eliza-scraping\xml_files\filters.csv"
urls_df = pd.read_csv(url_file_path)

# Assume the URLs are in a column named 'url'
urls = urls_df['url'].head(10000).tolist()  # Get only the first 10 URLs

# Initialize an empty list to store the results
results = []

# Loop through each URL and scrape the data
for url in urls:
    html = get_html(url)
    if html:
        details = property_details(html)
        results.append(details)  # Append the details to the results list
    else:
        print(f"Failed to retrieve HTML for {url}")

# Create a DataFrame from the results
df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
df.to_csv('property_details.csv', index=False)

print("Scraping completed. Data saved to 'property_details.csv'.")
