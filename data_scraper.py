from selenium import webdriver
import pandas as pd
import time
import os.path

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 800))  
display.start()
chromedriver_autoinstaller.install() 

chrome_options = webdriver.ChromeOptions()    
 
options = [
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get(ryan_url)
driver.implicitly_wait(5)

links = driver.find_elements_by_xpath("//*[contains(text(), '.csv')]")
ryan_link = links[0].get_attribute('href')
ryan_file = ryan_link[ryan_link.rfind('/')+1:]

f = open('links/links.txt', 'a')
f.write(ryan_file)

driver.get(vance_link)
driver.implicitly_wait(5)

links = driver.find_elements_by_xpath("//*[contains(text(), '.csv')]")
vance_link = links[0].get_attribute('href')
vance_file = vance_link[vance_link.rfind('/')+1:]

f.write(vance_link)
f.close()