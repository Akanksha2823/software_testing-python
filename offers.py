from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
driver.find_element(By.CLASS_NAME ,"_2GaeWJ").click()
#driver.find_element(By.CLASS_NAME,"H6-NpN _3N4_BX").click()