import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
driver.find_element(By.CLASS_NAME ,"Pke_EE").click()
driver.find_element(By.NAME, "q").send_keys("mobiles").click()
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button/svg").click()
time.sleep(3)
#driver.find_element(By.NAME, "q").send_keys("books")

#driver.find_element(By.LINK_TEXT ,"http://www.w3.org/2000/svg").get()