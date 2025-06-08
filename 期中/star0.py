import requests
from bs4 import BeautifulSoup
import threading

base_url = "https://tam.gov.taipei/News_Link_pic.aspx?n=B64052C7930D4913&sms=2CF1F5E2E0B96411&page={}&PageSize=6"

def fetch_page(page):
    url = base_url.format(page)
    r = requests.get(url)

    if r.status_code != 200:
        print(f"無法訪問: {url}")
        return
    
    soup = BeautifulSoup(r.text, "html.parser")
    sel = soup.select("div.essay a") 
    
    print(f"本頁的 URL: {url}")
    for link in sel:
        href = link.get("href")
        if href.startswith("http"): 
            full_url = href
        else:
            full_url = "https://tam.gov.taipei/" + href
        
        print("連結文字:", link.text.strip())
        print("連結:", full_url)

threads = []
for i in range(1, 11):
    thread = threading.Thread(target=fetch_page, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
