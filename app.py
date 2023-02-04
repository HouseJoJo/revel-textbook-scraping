from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import pandas as pd
import csv

def writeCSVtoTXT(read, write): #helper method to convert csv to .txt for end of program.
    with open(write, "w") as output_file:
        with open(read, "r") as input_file:
            csv_reader = csv.reader(input_file)
            for row in csv_reader:
                line = row[1]
                if(line[:1].isdigit()):
                    output_file.write("\n \n \n" + line)
                else: output_file.write("\n" + line)

#XPath key value pairs used during page navigation after sign in
xpaths = { 'openRevel' : "/html/body/div[1]/main/div[2]/div/div[2]/div/div[2]/div/div[4]/a[2]",
    'appPopUpClose' : "/html/body/appcues/div[2]/a",
    'osPopupClose': "/html/body/div[5]/div[2]/div/div[1]/button",
    'courseContentInput': "/html/body/div[2]/div/div[2]/div[4]/div[3]/div[1]/div[3]/div[2]/div/div",
    'ccInputChapters': "/html/body/div[5]/div[3]/ul/li[2]/div"}

#XPath key value pairs used when selecting a chapter to begin scraping. (Each one identified by specific IDs)
chapterPairsXpaths = {
    'chapter1' : '//*[@id="urn:pearson:entity:45f74f4e-81e4-43cf-8e32-0e21f775a565"]',
    'chapter2' : '//*[@id="urn:pearson:entity:6b72d958-d113-4784-91d6-2e3f51316bac"]',
    'chapter3' : '//*[@id="urn:pearson:entity:f588b056-e645-4a07-912a-b7251140a76a"]',
    'chapter4' : '//*[@id="urn:pearson:entity:105fa35d-7aaa-4a0a-b074-2c9c8b24da68"]',
    'chapter5' : '//*[@id="urn:pearson:entity:427850fb-ef08-43fa-9482-4f56909f6744"]',
    'chapter6' : '//*[@id="urn:pearson:entity:a1d0e218-9ba9-4199-84fa-e89cfb8f55d6"]',
    'chapter7' : '//*[@id="urn:pearson:entity:c04f2a5e-209f-454f-81e2-fa49cc8473ae"]',
    'chapter8' : '//*[@id="urn:pearson:entity:cebe5cfa-fa04-495e-a484-98f4be2e6e72"]',
    'chapter9' : '//*[@id="urn:pearson:entity:77be6df2-7c4e-4908-943c-fd0c02e51891"]',
    'chapter10' : '//*[@id="urn:pearson:entity:c521e0a3-2506-4a34-be5b-800453d8bd3f"]',
    'chapter11' : '//*[@id="urn:pearson:entity:972d3fbf-9074-41cf-a87e-5abe0da3a6fe"]',
    'chapter12' : '//*[@id="urn:pearson:entity:e0a8b39c-6b75-4bba-abd8-046c90293ca3"]',
    'chapter13' : '//*[@id="urn:pearson:entity:4de3bc9b-688a-4301-8e87-ce4d0d7fae54"]',
    'chapter14' : '//*[@id="urn:pearson:entity:8975028a-4f35-41f2-aec2-bec5d6050580"]',
    'chapter15' : '//*[@id="urn:pearson:entity:a399ae30-6a68-45c6-99e2-9b0f2801e7ad"]',
    'chapter16' : '//*[@id="urn:pearson:entity:2595c388-35a2-4dc9-8596-1dadd790addd"]',
    'chapter17' : '//*[@id="urn:pearson:entity:11aa0531-febb-4f5f-acde-4e2b0fea6964"]',
    'chapter18' : '//*[@id="urn:pearson:entity:4b961cab-7cd2-4ae2-95cb-46bbbd811f1b"]',
    'chapter19' : '//*[@id="urn:pearson:entity:4e9684f2-a53b-4730-8c2f-c8f2643a0308"]',
    'chapter20' : '//*[@id="urn:pearson:entity:630503b1-f831-4652-a314-4c5b14515283"]' }

driver = webdriver.Firefox()
driver.get("https://console.pearson.com/console/home") #Setup browser driver

elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#username")) #Wait for page to finish loading before logging in
)
validChapterStart = False #Variables needed for error-handling login inputs
intChapterStart = 0
while(not validChapterStart):
    try: #Checks chapter input. Needs to be within 1-20 (Specific to Connections textbook)
        chapterSelectStart = input("Enter what chapter number to start from (Ex: 1-20): ")
        if(1 <= int(chapterSelectStart) <= 20):
            intChapterStart = int(chapterSelectStart)
            chapterSelectStart = "chapter" + chapterSelectStart
            validChapterStart = True
        else:   print("Invalid input")
    except(ValueError):
        print("Invalid input")
validChapterEnd = False
while(not validChapterEnd):
    chapterSelectEnd = input("Enter to what chapter  number to collect the content from (Ex: 2-20 or 'end' for end of Ch.20): ")
    try: #Checks for ending chapter scrapping, Needs to be: an int & longer than start chapter, or 'end'.
        if(chapterSelectEnd == "end"):
            chapterSelectEnd = "Key Features"
            validChapterEnd = True
            print(chapterSelectEnd)
        elif(not chapterSelectStart.endswith("20") and 2 <= int(chapterSelectEnd) <= 20 and intChapterStart < int(chapterSelectEnd)):
            chapterSelectEnd = "Chapter " + chapterSelectEnd
            validChapterEnd = True
            print(chapterSelectEnd)
    except(ValueError):
        print("Invalid input")

ifLogin = True #Start of login error handling loop.
while(ifLogin):
    userinput = input("Enter Username to login:")
    passinput = input("Enter Password:") #Prompt user for credentials
    
    driver.find_element(By.CSS_SELECTOR,"#username").clear()
    driver.find_element(By.CSS_SELECTOR,"#password").clear()
    driver.find_element(By.CSS_SELECTOR,"#username").send_keys(userinput)
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys(passinput) #Input credentials and attempt login
    driver.find_element(By.CSS_SELECTOR,"#mainButton").click()
    try:
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH,xpaths["openRevel"])) #wait for browser to load next page
        )
        ifLogin = False #ends loop if exception not thrown.
        break
    except TimeoutException:
        print("Login failed. Try again.")
        driver.refresh()
print("Login success")

driver.find_element(By.XPATH,xpaths["openRevel"]).click() #Clicks to open assignment

WebDriverWait(driver, 30).until(
    EC.title_is("History 1111 - Spring 2023 - Dashboard") #Waits for page to load
)
print("Revel Dashboard loaded")

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

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH,xpaths["courseContentInput"])) #Waits for new page to load.
)
driver.find_element(By.XPATH,xpaths["courseContentInput"]).click()
driver.find_element(By.XPATH,xpaths["ccInputChapters"]).click() #Selects Chapter view on webpage

#Locates and enters chapter from previous user input.
driver.find_element(By.XPATH,chapterPairsXpaths[chapterSelectStart]).click()
driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div[2]/div/ul/li['+str(intChapterStart + 3)+']/div/div/div/ul/li[1]/button').click()
print("Entered desired chapter.")

#From this point forward, we should selects all titles, headers, and paragraph contents from page and
#compile them into a document.
templist = []
pageTitle = driver.title #Page titles will be updated and is used as our stopping condition.
while(chapterSelectEnd not in pageTitle): #While loop for ch.1 -> end crashes at about 15 chapters in on local machine.
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.assessment.assessmentLanding, div.player-content, div#assessementContainerBanner')) #waits for content page to load
    )
    if("Quiz" not in pageTitle): #condition only get data from non-quiz pages.
        try:
            templist.append(driver.find_element(By.CSS_SELECTOR, 'div.player-content h1').text) #collections first h1(Title)
        except NoSuchElementException:
            print("h1 was not found")
        try:
            templist.append(driver.find_element(By.CSS_SELECTOR, 'div.player-content h2').text) #collects first h2(sub-title)
        except NoSuchElementException:
            print("h2 was not found")
        content = driver.find_elements(By.CSS_SELECTOR, 'p.paragraphNumeroUno') #locates paragraph content
        for items in content:
            templist.append(items.text)
    driver.find_element(By.CSS_SELECTOR, 'div#nextPage button').click() #moves on to next page
    pageTitle = driver.title #updates title for eventual end to while loop

#The following takes all the data from the array and exports it to "table.csv". The .csv is then exported to
#"output.txt for readability"
df = pd.DataFrame(templist)
df.to_csv('table.csv')
driver.close()
writeCSVtoTXT('table.csv', 'output.txt') 