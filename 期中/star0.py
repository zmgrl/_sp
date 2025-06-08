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
    sel = soup.select("div.essay a")  # 確認選擇器是否正確
    
    print(f"本頁的 URL: {url}")
    for link in sel:
        href = link.get("href")
        if href.startswith("http"):  # 避免重複拼接完整網址
            full_url = href
        else:
            full_url = "https://tam.gov.taipei/" + href
        
        print("連結文字:", link.text.strip())
        print("連結:", full_url)

# 建立並行執行的多個執行緒
threads = []
for i in range(1, 11):
    thread = threading.Thread(target=fetch_page, args=(i,))
    threads.append(thread)
    thread.start()

# 確保所有執行緒完成
for thread in threads:
    thread.join()
