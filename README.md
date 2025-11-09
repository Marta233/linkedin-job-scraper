# 💼 LinkedIn Job Scraper

A **Python-based web scraper** that extracts job listings from **LinkedIn** based on user-specified **keywords** and **locations**.  
It provides an easy way to collect job data for analysis or portfolio projects — with results displayed in a **beautiful web interface** and exportable to **CSV**.

---

## 🚀 Features

- 🔍 Scrape jobs from LinkedIn by **keyword** and **location**
- 📊 Display a **sample of scraped jobs** in a clean HTML table
- 💾 **Export** full scraped data to CSV
- 🌐 **Flask web interface** for interactive use
- ⚙️ Built with **Selenium** for dynamic content scraping
- 🧹 Clean, structured output: **Title**, **Company**, **Location**, and **Link**

---

## 🛠️ Technologies Used

- 🐍 **Python 3.x**
- 🕸️ **Selenium** – for web automation and scraping  
- 🌐 **Flask** – to create the interactive web app  
- 📊 **Pandas** – for data processing and export  
- 🎨 **Bootstrap 5** – for responsive UI design  
- 💻 **ChromeDriver** – controls Chrome browser for scraping  

---

## 💾 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MARTA233/linkedin-job-scraper.git
cd linkedin-job-scraper
```
2️⃣ Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
```
Activate it:
```bash
.venv\Scripts\activate     # Windows
```
3️⃣ Install the required packages:
```bash
pip install -r requirements.txt
```
4️⃣ Download ChromeDriver

Download ChromeDriver matching your Chrome browser version and place it in an accessible location (e.g. C:\Windows\chromedriver.exe).


⚙️ Usage
▶️ Run the Flask web app

```bash
python app.py
```
Open your browser and go to: 

👉 http://127.0.0.1:5000

Steps:

Enter a keyword (e.g., Data Analyst)

Enter a location (e.g., Addis Ababa)

Click Scrape

After scraping completes:

Click 📊 Show Sample → to view the first 10 jobs in a table

Click ⬇️ Download CSV → to download all results

🧾 Example Output

| Title                 | Company  | Location    | Link                                         |
| --------------------- | -------- | ----------- | -------------------------------------------- |
| Data Analyst          | XYZ Ltd  | Addis Ababa | [View Job](https://linkedin.com/jobs/view/1) |
| Junior Data Scientist | ABC Corp | Addis Ababa | [View Job](https://linkedin.com/jobs/view/2) |

⚠️ Notes

🔐 LinkedIn may require manual login during scraping.

🧠 Use small job limits (e.g., max_jobs=50) to avoid being blocked.

🧩 Ensure ChromeDriver version matches your Chrome browser version.

⚖️ Please comply with LinkedIn’s Terms of Service
