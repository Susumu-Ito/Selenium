# モジュールのインポート
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# 初期化 : 初期化にはパスが必要
service = Service(executable_path="chromedriver")

# ChromeDriverの呼び出し
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
time.sleep(10)
driver.quit()
