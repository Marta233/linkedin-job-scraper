LinkedIn Job Scraper

A Python-based web scraper that extracts job listings from LinkedIn based on user-specified keywords and locations. This project provides an easy way to collect job data for analysis or portfolio purposes. The results can be displayed as a sample table in a web interface and exported as a CSV file.

🚀 Features

Scrape jobs from LinkedIn by keyword and location.

Display a sample of scraped jobs in a table format.

Export full scraped data to CSV.

Flask web interface for interactive use.

Built with Selenium for dynamic page scraping.

Clean and structured data: Title, Company, Location, and Link.

🛠️ Technologies Used

Python 3.x

Selenium – for web automation and scraping.

Flask – for web interface.

Pandas – for data storage and manipulation.

Bootstrap 5 – for responsive HTML tables and buttons.

ChromeDriver – to control Chrome browser.

💾 Installation

1. Clone the repository:
git clone https://github.com/MARTA233/linkedin-job-scraper.git
cd linkedin-job-scraper
2. Create a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
3. Install the required packages:
pip install -r requirements.txt
4. Download ChromeDriver and ensure it matches your Chrome version. Place the executable somewhere accessible, e.g., C:\Windows\chromedriver.exe
⚙️ Usage
1. Running the Flask Web App
python app.py
Open your browser and go to: http://127.0.0.1:5000

Enter the keyword (e.g., Data Analyst) and location (e.g., Addis Ababa).

Click Scrape.

After scraping:

Show Sample → displays the first 10 jobs in a table.

Download CSV → downloads the full scraped data.
