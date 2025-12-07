# Meta Threads Scraper with Automated GCS Upload<br><br>
This repository contains a robust Python pipeline designed to scrape posts from Meta Threads, clean the collected data, and automatically upload the results to Google Cloud Storage (GCS) for further analysis.<br><br>

# ✨ Features


Based on the codebase, this pipeline includes the following key capabilities:

Automated Scraping: Uses Selenium and BeautifulSoup4 for a robust, browser-based scraping process.

Anti-Detection Measures: Implements human-like behavior (random delays, viewport sizing, action chains, and scrolling variations) to minimize bot detection.

Targeted Search: Scrapes posts based on specified keywords (e.g., "일본", "韓国" for Japan and Korea).

Comprehensive Data Cleaning: Utilizes the Data_Cleanser module to:

Remove duplicate posts, empty posts, and short posts.

Filter out reply tags (Replying to @...).

Strip websites, URLs, and emojis.

Language Detection: Attempts to identify the target country/language of the scraped content using langdetect.

Cloud Integration: Seamlessly uploads the cleaned data as a CSV file to a designated Google Cloud Storage (GCS) bucket.<br><br>



# 🛠️ Installation and Setup


**1. Prerequisites**
You need Python 3.x installed, and since the scraper uses Selenium, you will need a compatible web browser like Google Chrome installed on your system or environment.

**2. Dependencies**
Install the required Python packages using pip:

Bash

pip install -r requirements.txt
The key dependencies include selenium, webdriver-manager, google-cloud-storage, beautifulsoup4, pandas, and python-dotenv.

**3. Configuration (.env file)**
This project requires sensitive credentials to be stored as environment variables in a file named .env in the root directory.

Create a file named .env and populate it with your credentials:

Ini, TOML

**Threads Credentials **
THREADS_USERNAME="your_threads_username"
THREADS_PASSWORD="your_threads_password"

**Google Cloud Storage Configuration**
BUCKET_NAME="your-gcs-bucket-name"

**Path to your GCP Service Account Key file (JSON)**
**Ensure this file is accessible by the script.**
GCP_CREDENTIALS="/path/to/your/gcp-service-account-key.json"<br><br>


# 🚀 Usage
The pipeline is executed via the main.py file.

Define Keywords: Modify the TARGET_KEYWORD list in main.py to set the terms you wish to scrape (e.g., TARGET_KEYWORD = ["your_term_1", "your_term_2"]).

Define Post Count: Adjust TARGET_POSTS_NUM in main.py to set the desired number of posts to scrape per keyword.

Run the script:

Bash

python main.py
Data Flow
The main function executes the following process for each configured keyword :

**Login:** Connects and logs into Threads.

**Scrape:** Uses the ThreadsScraper to search for the keyword, scroll, and collect raw posts.

**Clean:** Passes the raw data to the Data_Cleanser to remove noise and unwanted content.

**Upload:** The resulting cleaned DataFrame is converted to a CSV string and uploaded to GCS under the path: raw-data/{keyword}_{YYYY-MM-DD}.csv.<br><br>

# 📄 License
This project is licensed under the Apache License, Version 2.0.
