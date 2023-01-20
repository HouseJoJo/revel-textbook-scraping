from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://console.pearson.com/console/home")

elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#username"))
)
username = driver.find_element(By.CSS_SELECTOR,"#username")
#username.send_keys("username")
password = driver.find_element(By.CSS_SELECTOR,"#password")
#password.send_keys("password")
print("something?")
print(username.get_attribute("outerHTML"))
print(password.get_attribute("outerHTML"))
driver.close()