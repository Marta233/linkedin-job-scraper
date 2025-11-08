from flask import Flask, render_template, request, send_file
from scraper import LinkedInScraper
import pandas as pd
from urllib.parse import quote_plus
import os

app = Flask(__name__, template_folder="templates")

CHROMEDRIVER_PATH = r"C:\Windows\chromedriver.exe"
DATA_FILE = "linkedin_jobs.csv"
latest_df = pd.DataFrame()
last_keyword = ""
last_location = ""


@app.route("/", methods=["GET", "POST"])
def index():
    global latest_df, last_keyword, last_location
    table_html = None
    message = None
    scraped = False

    # Load existing CSV if available when the app starts
    if latest_df.empty and os.path.exists(DATA_FILE):
        latest_df = pd.read_csv(DATA_FILE)
        scraped = True

    if request.method == "POST":
        action = request.form.get("action")

        # ---------- SCRAPE NEW DATA ----------
        if action == "scrape":
            keyword = request.form.get("keyword", "").strip()
            location = request.form.get("location", "").strip()

            if not keyword or not location:
                message = "⚠️ Please provide both keyword and location."
                return render_template("index.html",
                                       message=message,
                                       scraped=not latest_df.empty,
                                       keyword=last_keyword,
                                       location=last_location)

            q = quote_plus(keyword)
            loc = quote_plus(location)
            url = f"https://www.linkedin.com/jobs/search/?keywords={q}&location={loc}"

            scraper = LinkedInScraper(url=url, chromedriver_path=CHROMEDRIVER_PATH, max_jobs=50)

            try:
                scraper.setup_driver(headless=False)
                scraper.open_page()
                scraper.scroll_page(times=5)
                scraper.extract_jobs()
                latest_df = scraper.get_jobs_dataframe()
            except Exception as e:
                message = f"❌ Error during scraping: {str(e)}"
                latest_df = pd.DataFrame()
            finally:
                scraper.close_driver()

            if not latest_df.empty:
                latest_df.to_csv(DATA_FILE, index=False)
                last_keyword, last_location = keyword, location
                message = f"✅ Successfully scraped {len(latest_df)} jobs for '{keyword}' in '{location}'."
                scraped = True
            else:
                message = "⚠️ No jobs found. Please try another search."

        # ---------- SHOW SAMPLE ----------
        elif action == "sample":
            if latest_df.empty and os.path.exists(DATA_FILE):
                latest_df = pd.read_csv(DATA_FILE)

            if not latest_df.empty:
                table_html = latest_df.head(10).to_html(
                    classes="table table-striped table-bordered",
                    index=False,
                    escape=False
                )
                message = f"📋 Showing first 10 of {len(latest_df)} scraped jobs."
                scraped = True
            else:
                message = "⚠️ No scraped data available. Please scrape first."

        # ---------- DOWNLOAD CSV ----------
        elif action == "download":
            if os.path.exists(DATA_FILE):
                return send_file(DATA_FILE, as_attachment=True)
            else:
                message = "⚠️ No CSV file found. Please scrape first."

    return render_template(
        "index.html",
        message=message,
        table=table_html,
        scraped=not latest_df.empty,
        keyword=last_keyword,
        location=last_location
    )


if __name__ == "__main__":
    app.run(debug=True)
