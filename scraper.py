# scraper.py
import time
import random
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkedInScraper:
    def __init__(self, url, chromedriver_path, max_jobs=50):
        self.url = url
        self.chromedriver_path = chromedriver_path
        self.max_jobs = max_jobs
        self.driver = None
        self.jobs = []

    def human_sleep(self, a=0.5, b=1.2):
        time.sleep(random.uniform(a, b))

    def setup_driver(self, headless=False):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # reduce detection surface
        options.add_argument("--disable-blink-features=AutomationControlled")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        service = Service(self.chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver

    def open_page(self):
        if not self.driver:
            raise Exception("Driver not initialized.")
        self.driver.get(self.url)
        # allow user to log in manually if required
        time.sleep(8)

    def scroll_page(self, times=5):
        if not self.driver:
            raise Exception("Driver not initialized.")
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight/3);")
            self.human_sleep(1, 2)

    def clean_text(self, text):
        if not text:
            return ""
        # remove newlines/tabs and collapse multiple whitespace to single space
        cleaned = re.sub(r'\s+', ' ', text)
        return cleaned.strip()

    def extract_jobs(self):
        """Fill self.jobs with cleaned dicts. No debug prints of raw HTML."""
        if not self.driver:
            raise Exception("Driver not initialized.")
        wait = WebDriverWait(self.driver, 12)
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.jobs-search__results-list")))
        except:
            # Try to continue even if not found — LinkedIn layout may differ
            pass

        # possible selectors for job cards
        selectors = [
            "ul.jobs-search__results-list li",
            "div.job-card-container--clickable",
            "li.job-result-card"
        ]
        cards = []
        for sel in selectors:
            found = self.driver.find_elements(By.CSS_SELECTOR, sel)
            if found:
                cards = found
                break

        self.jobs = []
        for card in cards[:self.max_jobs]:
            try:
                # re-locate or scroll into view to reduce stale reference issues
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
                self.human_sleep(0.25, 0.7)

                # get text safely
                try:
                    title = card.find_element(By.CSS_SELECTOR, "h3").text
                except:
                    title = ""
                try:
                    company = card.find_element(By.CSS_SELECTOR, "h4").text
                except:
                    company = ""
                try:
                    location = card.find_element(By.CSS_SELECTOR, "span.job-search-card__location, span.job-card-container__metadata-item").text
                except:
                    location = ""
                try:
                    link = card.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                except:
                    link = ""

                # clean fields
                title = self.clean_text(title)
                company = self.clean_text(company)
                location = self.clean_text(location)

                # only append when there is some title or link
                if title or link:
                    self.jobs.append({
                        "Title": title,
                        "Company": company,
                        "Location": location,
                        "Link": link
                    })

            except Exception:
                # skip problematic card
                continue

    def get_jobs_dataframe(self):
        if not self.jobs:
            return pd.DataFrame(columns=["Title", "Company", "Location", "Link"])
        return pd.DataFrame(self.jobs)

    def close_driver(self):
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
