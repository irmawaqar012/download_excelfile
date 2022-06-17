from os import path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
# import openpyxl

chromeOptions = webdriver. ChromeOptions()
prefs = {"download.default_directory" : "E:\\PythonPractice\\download_excelfile"}
# C:\\Users\\Aamir Trader\'s\\Downloads
chromeOptions. add_experimental_option("prefs",prefs)
# chromedriver = "path/to/chromedriver.exe"
# driver = webdriver.Chrome(executable_path="E:\PythonPractice\download_excelfile", options = chromeOptions)


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


# driver.maximize_window()

# download excel file
driver.find_element_by_id("txtReport").click()
time.sleep(0.5)
driver.find_element_by_id("txtMonthly").click()
time.sleep(0.5)
driver.find_element_by_id("MainContent_Button15").click()
time.sleep(60)

# path=  "C:\Users\Aamir Trader's\Downloads\Data_inOut.xls"
# wb=openpyxl.load_workbook(path)
# sheet=wb.active
# rows=sheet.max_row
# cols=sheet.max_column

# for r in range(1, rows+1):
#     for c in range(1, cols+1):
#         print(sheet.cell(row=r, cloumn=c).value, end="   ")
#         print()

# print(rows)
# print(cols)
# f = open("MainContent_Button15", "r")
# time.sleep(3)
# print(f)
# time.sleep(3)


  

driver.close()

