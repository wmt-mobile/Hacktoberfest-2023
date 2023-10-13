from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import csv
from selenium.webdriver.support import expected_conditions as EC
import json
import time

URL = "https://www.freshersnow.com/machine-learning-mcqs-and-answers-with-explanation/"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(URL)
r = 3
i = 4


templist = []
templist2 = []
templist3 = []


while(r < 119):
    print(r)
    driver.implicitly_wait(6)
 
    ans = driver.find_element(
        By.XPATH, f'//*[@id="post-566124"]/div[2]/div[2]/p[{r}]/strong')

    ans1 = driver.find_element(
        By.XPATH, f'//*[@id="post-566124"]/div[2]/div[2]/p[{i}]')

    # ans2 = driver.find_element(
    #     By.CSS_SELECTOR, f"body > div.page-wrapper > div.page-content > section > div > div.row.mt-20 > div.col-12.col-lg-6.mb-6.mb-lg-0.interview-block > div:nth-child(1) > div:nth-child({i}) > div > ul > li.answer")

    templist.append(ans.text)
    templist2.append(ans1.text)
    # templist3.append(ans2.text)
   
    r += 4
    i += 4
    


html = driver.page_source


filez = open("AI.csv", "a")
writer = csv.writer(filez)

for w in range(len(templist)):
    writer.writerow([templist[w], templist2[w]])


templist = json.dumps(templist)
print(templist)