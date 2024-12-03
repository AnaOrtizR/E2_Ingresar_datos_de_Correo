from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://promusic.cl/account/login")

usuario = driver.find_element(By.ID, "CustomerEmail")
usuario.send_keys("ana.ortiz.romo@gmail.com")
usuario.send_keys(Keys.RETURN)
time.sleep(1)


clave = driver.find_element(By.ID, "CustomerPassword")
clave.send_keys("PMAO2588")
clave.send_keys(Keys.RETURN)
time.sleep(2)
driver.close()