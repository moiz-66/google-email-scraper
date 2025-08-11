from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time,random
import  os
import re
import pandas as pd
from urllib.parse import urljoin
from validate_email import validate_email

def extract_info(url):

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(headless = False,channel='chrome',user_data_dir='C:/Users\dell\AppData\Local\Google\Chrome/User Data\Profile 3')
        page = browser.new_page()
        page.goto(url,timeout=60000,wait_until="domcontentloaded")
        time.sleep(random.uniform(0.5,1.5))
        page.wait_for_selector("div#search h3", timeout=0)
        page.wait_for_timeout(random.uniform(100.314,300.8273))
        html = page.content()
        # context.storage_state(path = cookies_file)

        return html
def parse_html(html):
    full_data = []
    soup = BeautifulSoup(html,"html.parser")
    name = soup.find_all("h3",class_="LC20lb MBeuO DKV0Md")
    email = soup.find_all("div",class_="VwiC3b yXK7lf p4wth r025kc hJNv6b Hdw6tb")
    for n,e in zip(name,email):
        full_name = n.text.strip()
        email = e.text.strip()
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email)
        valid_emails = [email for email in emails if email.endswith("comcast.net")]
        if not valid_emails:
            continue
        cleaned_text = re.sub(r'\(\d{3}\)\s*\d{3}-\d{4}', '', full_name).strip()
        cleaned_text = re.sub(r'\s*-\s*$', '', cleaned_text)
        for email in valid_emails:
            if is_valid_email(email):

                data = {"full name":cleaned_text,"email":email}
                full_data.append(data)
    print(full_data)
    return full_data

def is_valid_email(email):
    return validate_email(email)

def save_to_csv(data, file_path="file1.csv"):
    df = pd.DataFrame(data)
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)


def main():
    urls = ['https://www.google.com/search?q=%22Jordan+%22+%22%40comcast.net%22+site%3Afamilytreenow.com&sca_esv=8011337b228d5ddd&biw=1737&bih=795&sxsrf=AE3TifMddHCtD5BI2Sv9c3zqGjsPbXO8qw%3A1754760971365&ei=C4eXaNKIFvPXi-gPyom2qAM&ved=0ahUKEwiSuvSCov6OAxXz6wIHHcqEDTUQ4dUDCBA&uact=5&oq=%22Jordan+%22+%22%40comcast.net%22+site%3Afamilytreenow.com&gs_lp=Egxnd3Mtd2l6LXNlcnAiLyJKb3JkYW4gIiAiQGNvbWNhc3QubmV0IiBzaXRlOmZhbWlseXRyZWVub3cuY29tSLEWUO0OWO0OcAJ4AJABAJgB-gGgAfoBqgEDMi0xuAEDyAEA-AEC-AEBmAIAoAIAmAMAiAYBkgcAoActsgcAuAcAwgcAyAcA&sclient=gws-wiz-serp' ]
    for url in urls:
        time.sleep(random.uniform(4,7.7))
        while True:
            html = extract_info(url)
            data = parse_html(html)
            save_to_csv(data)
            soup = BeautifulSoup(html,"html.parser")
            next_tag = soup.find("a", id="pnnext")
            if next_tag:
                link = urljoin("https://www.google.com",next_tag.get("href"))
                if link:
                    url = link
                else:
                    break
            else:
                break
if __name__ == "__main__":
    main()
