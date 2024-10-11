# Immo Eliza Scraping

## 📖 Overview
Immo Eliza Scraping is a web scraping project designed to extract real estate listings from the Immoweb website. The project collects property details, including information on houses and apartments for sale, and stores them in a CSV file for easy access and analysis.

## Features
- Scrapes property URLs from multiple XML sitemaps provided by Immoweb.
- Filters the extracted URLs to focus on houses and apartments for sale.
- Collects detailed property information, including:
  - Property ID
  - Locality name
  - Postal Code
  - Price
  - Type of proterty (house or apartment)
  - Subtype of property (bungalow, chalet, mansion,...)
  - Type of sale (note: exclude life sales)
  - Number of rooms
  - Living area (area in m²)
  - Equipped kitchen (0/1)
  - Furnished (0/1)
  - Open fire (0/1)
  - Terrace (area in m² or null if no terrace)
  - Garden (area in m² or null if no garden)
  - Number of facades
  - Swimming pool (0/1)
  - State of building (new, to be renovated, ...)
- Saves the extracted data into a CSV file for further analysis or reporting.

## 📦 Repo structure

```
.
├── data/
│ └── extracted_details.csv
│ └── filters.csv
│ └── property_details.csv
├── scraper/
│ └── accept_cookies.ipynb
  └── filtered_urls.ipynb
│ └── one_house_immoweb.ipynb
│ └── properties_details.ipynb
│ └── scraper.py
├── .gitignore
├── chromedriver.exe
├── main.py
├── README.md
└── requirements.txt
```

## 🛠 Installation

### Prerequisites
- Python 3.6 or higher
- `pandas` library
- `requests` library
- `BeautifulSoup` library from `bs4`

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd immo-eliza-scraping
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install pandas requests beautifulsoup4 lxml
   ```

## 🚀 Usage

1. **Download XML files**:
   - Run the script `filtred_urls.ipynb` to download the XML sitemap files and extract property URLs:

2. **Filter URLs**:
   - The filtered URLs are saved in `filters.csv`.

3. **Scrape Property Details**:
   - Run the script `main.py` to scrape detailed information from the filtered property URLs:

4. **Output**:
   - The scraped property details will be saved in `property_details.csv`.

## 🔍 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or open an issue.

## 📜 Timeline

This project was completed as part of the AI Boocamp at BeCode.org in 5 days