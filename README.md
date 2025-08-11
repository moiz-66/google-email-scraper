Google Email Scraper – Playwright + BeautifulSoup

Description:
------------
This Python script automates Google searches using Playwright with your real Chrome profile. 
It extracts names and comcast.net email addresses from search results and saves them to a CSV file.
The script handles pagination automatically and validates emails before saving.

Features:
---------
- Uses your real Chrome browser profile (no manual cookies needed)
- Scrapes Google search result names and emails
- Filters for comcast.net email addresses
- Validates emails with `validate_email`
- Handles multiple pages automatically
- Saves results to CSV (append mode if file exists)

Requirements:
-------------
- Python 3.8+
- Google Chrome installed
- Chrome profile path (update in the code: `user_data_dir` variable)
- Python packages:
    playwright
    beautifulsoup4
    pandas
    validate_email

Installation:
-------------
1. Install Python packages:
   pip install playwright beautifulsoup4 pandas validate_email

2. Install Playwright browsers:
   playwright install

3. Edit the `user_data_dir` in `extract_info()` with the path to your Chrome profile.
   Example:
   C:/Users/YourUser/AppData/Local/Google/Chrome/User Data/Profile 3

4. Update the `urls` list in `main()` with your desired Google search query.

Usage:
------
1. Open terminal in the script's directory.
2. Run:
   python script_name.py

3. The output file (file1.csv) will contain:
   full name, email

Notes:
------
- This script scrapes Google; frequent searches may trigger captchas.
- Increase sleep times between requests to avoid blocking.
- Google and target website layouts may change, so selectors might need updates.
- Respect terms of service of the websites you scrape.
