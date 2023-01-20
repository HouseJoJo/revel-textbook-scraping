from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

xpath = { 'openRevel' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]",
    'openRevelAlt' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]/span",
    'closeAlert1Bttn' : "/html/body/div[5]/div[2]/div/div[1]/button",
    'continueReadingBttn' : "/html/body/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div/div[2]/div/div/div/button" }

driver = webdriver.Firefox()
driver.get("https://console.pearson.com/console/home")

elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#username"))
)
username = driver.find_element(By.CSS_SELECTOR,"#username")
#username.send_keys("username")
password = driver.find_element(By.CSS_SELECTOR,"#password")
loginbttn = driver.find_element(By.CSS_SELECTOR,"#mainButton")
#password.send_keys("password")

userinput = input("Enter Username to login:")
passinput = input("Enter Password:")

print(userinput)
print(passinput)

username.send_keys(userinput)
password.send_keys(passinput)
loginbttn.click()

#print(username.get_attribute("outerHTML"))
#print(password.get_attribute("outerHTML"))