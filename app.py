from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

xpath = { 'openRevel' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]",
    'openRevelAlt' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]/span",
    'closeAlert1Bttn' : "/html/body/div[5]/div[2]/div/div[1]/button",
    'continueReadingBttn' : "/html/body/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div/div[2]/div/div/div/button" }
#Storing xpaths for future use.

driver = webdriver.Firefox()
driver.get("https://console.pearson.com/console/home")
#setup driver w/ webpage

elem = WebDriverWait(driver, 30).until( #wait for page to load
    EC.presence_of_element_located((By.CSS_SELECTOR,"#username"))
)

username = driver.find_element(By.CSS_SELECTOR,"#username")
password = driver.find_element(By.CSS_SELECTOR,"#password")
loginbttn = driver.find_element(By.CSS_SELECTOR,"#mainButton")
#grab elements required to login

userinput = input("Enter Username to login:")
passinput = input("Enter Password:") #ask user for credentials

username.send_keys(userinput)
password.send_keys(passinput)
loginbttn.click() #login attempt.

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#courseCardContainer"))
        or EC.presence_of_all_elements_located((By.CSS_SELECTOR,"p.ng-binding"))
    )
except selenium.common.exceptions.StaleElementReferenceException:
    print("Expected error")

while(EC.url_contains("login")):
    username.clear()
    password.clear()
    print("Failed login. Try again")
    userinput = input("Enter Username to login:")
    passinput = input("Enter Password:")

    username.send_keys(userinput)
    password.send_keys(passinput)
    loginbttn.click()

    try:
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#courseCardContainer"))
        or EC.presence_of_all_elements_located((By.CSS_SELECTOR,"p.ng-binding"))
        )
    except selenium.common.exceptions.StaleElementReferenceException:
        print("Expected error")

driver.close()
#print(username.get_attribute("outerHTML"))
#print(password.get_attribute("outerHTML"))