from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import os

URL = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en"

options = Options()
options.add_argument("--window-size=1920,1080")
options.page_load_strategy = "eager"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.set_page_load_timeout(60)

try:
    driver.get(URL)
    time.sleep(8)

    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    cards = driver.find_elements(By.CSS_SELECTOR, "h2, h3")
    print("Elements found:", len(cards))

    products = []
    for c in cards:
        text = c.text.strip()
        if len(text) > 5:
            products.append({
                "product_name": text,
                "source": "Alibaba"
            })

    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/alibaba_raw.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    print(f"✅ Saved {len(products)} products")

finally:
    driver.quit()
