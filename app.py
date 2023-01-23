from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

xpaths = { 'openRevel' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]",
    'openRevelAlt' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]/span",
    'closeAlert1Bttn' : "/html/body/div[5]/div[2]/div/div[1]/button",
    'continueReadingBttn' : "/html/body/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div/div[2]/div/div/div/button",
    'appPopUp' : "/html/body/appcues",
    'appPopUpClose' : "/html/body/appcues/div[2]/a",
    'osPopupClose': "/html/body/div[5]/div[2]/div/div[1]/button",
    'courseContentInput': "/html/body/div[2]/div/div[2]/div[4]/div[3]/div[1]/div[3]/div[2]/div/div",
    'ccInputChapters': "/html/body/div[5]/div[3]/ul/li[2]/div"}
    #Pairs of xpaths for future use.

driver = webdriver.Firefox()
driver.get("https://console.pearson.com/console/home") #Setup browser driver

elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#username")) #Wait for page to finish loading
)

username = driver.find_element(By.CSS_SELECTOR,"#username")
password = driver.find_element(By.CSS_SELECTOR,"#password")
loginbttn = driver.find_element(By.CSS_SELECTOR,"#mainButton") #Select elements needed for login

userinput = input("Enter Username to login:")
passinput = input("Enter Password:") #Prompt user for credentials

username.send_keys(userinput)
password.send_keys(passinput) #Input credentials and attempt login
loginbttn.click()

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH,xpaths["openRevel"])) #wait for browser to load next page
)
print("Login success")

driver.find_element(By.XPATH,xpaths["openRevel"]).click() #Clicks to open assignment

WebDriverWait(driver, 30).until(
    EC.title_is("History 1111 - Spring 2023 - Dashboard") #Waits for page to load
)
print("Revel Content loaded")
try:
    driver.find_element(By.XPATH,xpaths['appPopUpClose']).click()
    print("App popup closed")
except NoSuchElementException:
    print("App popup not found")

try:
    driver.find_element(By.XPATH,xpaths["osPopupClose"]).click()
    print("OS popup closed")
except NoSuchElementException:
    print("OS popup not found")

print("Final")
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH,xpaths["courseContentInput"]))
)
driver.find_element(By.XPATH,xpaths["courseContentInput"]).click()

driver.find_element(By.XPATH,xpaths["ccInputChapters"]).click()
print("All chapters selected")