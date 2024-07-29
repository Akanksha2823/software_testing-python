from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
driver.find_element(By.LINK_TEXT ,"Login").click()
driver.find_element(By.CLASS_NAME ,"r4vIwl BV+Dqf").send_keys("8217262565")
#driver.find_element(By.NAME, "q").send_keys("mobiles")