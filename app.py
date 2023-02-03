from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import csv

def writeCSVtoTXT(read, write): #helper text to convert csv to .txt
    with open(write, "w") as output_file:
        with open(read, "r") as input_file:
            csv_reader = csv.reader(input_file)
            for row in csv_reader:
                line = row[1]
                if(line[:1].isdigit()):
                       output_file.write("\n \n \n" + line)
                else: output_file.write("\n" + line)

xpaths = { 'openRevel' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]",
    'openRevelAlt' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]/span",
    'closeAlert1Bttn' : "/html/body/div[5]/div[2]/div/div[1]/button",
    'continueReadingBttn' : "/html/body/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div/div[2]/div/div/div/button",
    'appPopUp' : "/html/body/appcues",
    'appPopUpClose' : "/html/body/appcues/div[2]/a",
    'osPopupClose': "/html/body/div[5]/div[2]/div/div[1]/button",
    'courseContentInput': "/html/body/div[2]/div/div[2]/div[4]/div[3]/div[1]/div[3]/div[2]/div/div",
    'ccInputChapters': "/html/body/div[5]/div[3]/ul/li[2]/div",
    'chapter1Selection': '//*[@id="urn:pearson:entity:45f74f4e-81e4-43cf-8e32-0e21f775a565"]',
    'chapter1-1Selection': "/html/body/div[2]/div/div[2]/div[4]/div[3]/div[2]/div/ul/li[4]/div/div/div/ul/li[1]/button" }
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
    driver.find_element(By.XPATH,xpaths['appPopUpClose']).click() #Block closes a potential app pop-up
    print("App popup closed")
except NoSuchElementException:
    print("App popup not found")

try:
    driver.find_element(By.XPATH,xpaths["osPopupClose"]).click() #Code block closes any "incompatible OS" pop-ups
    print("OS popup closed")
except NoSuchElementException:
    print("OS popup not found")

print("Final")
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH,xpaths["courseContentInput"])) #Waits for new page to load.
)
driver.find_element(By.XPATH,xpaths["courseContentInput"]).click()
driver.find_element(By.XPATH,xpaths["ccInputChapters"]).click() #Selects Chapter view on webpage

print("All chapters selected")

driver.find_element(By.XPATH,xpaths['chapter1Selection']).click()
driver.find_element(By.XPATH,xpaths["chapter1-1Selection"]).click() #Locates and enters Chapter 1.1
print("Entered chapter 1.1")

#From this point forward, we should selects all titles, headers, and paragraph contents from page and
#compile them into a document. Either create an array for each chapter, and an array to compile all chapters.
templist = []
pageTitle = driver.title
while("Chapter 2" not in pageTitle):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.assessment.assessmentLanding, div.player-content, div#assessementContainerBanner')) #waits for content page to load
    )
    if("Quiz" not in pageTitle):
        try:
            templist.append(driver.find_element(By.CSS_SELECTOR, 'div.player-content h1').text) #collections first h1(Title)
        except NoSuchElementException:
            print("h1 was not found")
        try:
            templist.append(driver.find_element(By.CSS_SELECTOR, 'div.player-content h2').text) #collects first h2(sub-title)
        except NoSuchElementException:
            print("h2 was not found")
        content = driver.find_elements(By.CSS_SELECTOR, 'p.paragraphNumeroUno') #saves content
        for items in content:
            templist.append(items.text)
    driver.find_element(By.CSS_SELECTOR, 'div#nextPage button').click()
    pageTitle = driver.title
df = pd.DataFrame(templist)
df.to_csv('table.csv')
driver.close()
writeCSVtoTXT('table.csv', 'output.txt')
