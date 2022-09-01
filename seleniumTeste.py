from sys import executable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r"C:\Users\guilh\AppData\Local\Programs\Python\Python310\chromedriver.exe")
driver.get("https://www.google.com.br")
driver.find_element("name", "q").send_keys("Testes automatizados" + Keys.RETURN)
driver.find_element(By.XPATH, "//*[@id='rso']/div[4]/div/div/div/div[1]/div/a").click()