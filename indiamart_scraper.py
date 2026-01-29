from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, json, os, random

URL = "https://dir.indiamart.com/impcat/electrical-panels.html"

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get(URL)
time.sleep(5)

# options.add_argument("--headless")

# SCROLL to trigger lazy loading
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

cards = driver.find_elements(By.CSS_SELECTOR, "div.lst_cl")
print(f"Found {len(cards)} products")

products = []

for card in cards:
    try:
        name = card.find_element(By.TAG_NAME, "h3").text
    except:
        name = None

    try:
        price = card.find_element(By.CLASS_NAME, "prc").text
    except:
        price = None

    try:
        supplier = card.find_element(By.CLASS_NAME, "company-name").text
    except:
        supplier = None

    try:
        location = card.find_element(By.CLASS_NAME, "newLocationUi").text
    except:
        location = None

    products.append({
        "product_name": name,
        "price": price,
        "supplier": supplier,
        "location": location
    })

driver.quit()

os.makedirs("data/raw", exist_ok=True)
with open("data/raw/indiamart_electrical_raw.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print("Scraping completed successfully.")



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import json
# import os
# import random

# BASE_URL = "https://dir.indiamart.com/impcat/brick-making-machines.html"

# def get_driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=1920,1080")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")

#     return webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=chrome_options
#     )

# def scrape_indiamart():
#     driver = get_driver()
#     driver.get(BASE_URL)
#     time.sleep(5)

#     products = []

#     cards = driver.find_elements(By.CSS_SELECTOR, "div.card")
#     print(f"Found {len(cards)} products")

#     for card in cards:
#         try:
#             product_name = card.find_element(By.TAG_NAME, "h3").text
#         except:
#             product_name = None

#         try:
#             price = card.find_element(By.CLASS_NAME, "prc").text
#         except:
#             price = None

#         try:
#             supplier = card.find_element(By.CLASS_NAME, "company-name").text
#         except:
#             supplier = None

#         try:
#             location = card.find_element(By.CLASS_NAME, "newLocationUi").text
#         except:
#             location = None

#         products.append({
#             "product_name": product_name,
#             "price": price,
#             "supplier": supplier,
#             "location": location
#         })

#         time.sleep(random.uniform(1, 2))

#     driver.quit()

#     os.makedirs("data/raw", exist_ok=True)
#     with open("data/raw/indiamart_electrical_raw.json", "w", encoding="utf-8") as f:
#         json.dump(products, f, indent=4, ensure_ascii=False)

#     print("Scraping completed.")

# if __name__ == "__main__":
#     scrape_indiamart()
