#インポート
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初期化
service = Service(executable_path="chromedriver")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-loging'])

# ChromeDriverの呼び出し
driver = webdriver.Chrome(service=service,options=options)
driver.get("https://www.google.com")

#要素の出現を待つ
WebDriverWait(driver,10).until(
  EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

#文字を入力
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("TestTest" + Keys.ENTER)

time.sleep(5)
driver.quit()


