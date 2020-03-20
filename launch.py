from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.sudoku.com/expert/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))

newgame = driver.find_element_by_class_name("game-cell")
newgame.click()

#one = driver.find_element_by_class_name("numpad-item")
#one.click()

for row in driver.find_elements_by_css_selector("tr.game-row"):
    cell = row.find_elements_by_tag_name("td.game-cell.game-value")
    print(cell[0])
