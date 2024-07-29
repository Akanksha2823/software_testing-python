from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com/")
#driver.find_element(By.id ,"twotabsearchtextbox").click()
#driver.find_element(By.id , "twotabsearchtextbox").send_keys("mobile").click()
#driver.find_element(By.CLASS_NAME ,"nav-action-inner").click()

#driver.find_element(By.NAME, "q").send_keys("mobiles")