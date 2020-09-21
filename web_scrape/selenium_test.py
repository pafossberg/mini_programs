from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://ubuntu.com/')

search = driver.find_element_by_name('q')
search.send_keys('test')
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )
    titles = main.find_elements_by_class_name("title-main")
    for title in titles:
        print(title.text)

finally:
    driver.quit()
