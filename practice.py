from lib2to3.pgen2.driver import Driver
from os import path
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import openpyxl as O

chromeOptions = webdriver. ChromeOptions()
folder_path=os.path.dirname(os.path.abspath(__file__))

prefs = {"download.default_directory" : folder_path}
chromeOptions. add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(ChromeDriverManager().install(), options = chromeOptions)

driver.get("https://cloud.amts.pk/")

time.sleep(0.5)

# Login screen
driver.find_element_by_id("TextBox1").send_keys("excelorithm")
time.sleep(0.2)
driver.find_element_by_id("TextBox2").send_keys("irma")
time.sleep(0.2)
driver.find_element_by_id("TextBox3").send_keys("Irma123**")
time.sleep(0.2)
driver.find_element_by_id("Button1").click()
time.sleep(1)

# download excel file
driver.find_element_by_id("txtReport").click()
time.sleep(0.5)
driver.find_element_by_id("txtMonthly").click()
time.sleep(0.5)
driver.find_element_by_id("MainContent_Button15").click()
time.sleep(30)





driver.close()
driver.quit()

