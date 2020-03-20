from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.sudoku.com")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))

newgame = driver.find_element_by_class_name("game-cell")
newgame.click()

one = driver.find_element_by_class_name("numpad-item")
one.click()
