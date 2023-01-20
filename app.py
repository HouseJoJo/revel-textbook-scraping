from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://console.pearson.com/console/home")

username = driver.find_element(By.CSS_SELECTOR,"input#username")
#Above does not work. Look into selecting by xcom
print(username)
#username.send_keys("username")

password = driver.find_element(By.CSS_SELECTOR,"input#password")
print(password)
#username.send_keys("password")