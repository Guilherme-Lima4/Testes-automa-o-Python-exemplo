from sys import executable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r"C:\Users\guilh\AppData\Local\Programs\Python\Python310\chromedriver.exe")
driver.get("https://blog.geekhunter.com.br/as-maiores-vantagens-de-testes-automatizados/")
