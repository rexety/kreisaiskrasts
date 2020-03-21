from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import numpy as np
import time
empty_base = np.zeros(shape=(9,9))


keys = []
for i in range(1,10):
    keys.append(i)
vectordic = dict.fromkeys(keys)

f = open("vectorpaths.txt").read().splitlines()

temp = 1
for x in f:
    vectordic[temp] = x
    temp += 1
    if temp == 10:
        break
    
    

driver = webdriver.Chrome()
driver.get("http://www.sudoku.com/easy/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))

newgame = driver.find_element_by_class_name("game-cell")
newgame.click()
newgame.send_keys(Keys.NUMPAD2)

#through dynamic xpath iterate over whole 9x9 matrix, if empty put zero else read vector path

for row in range(1,10):
    for cell in range(1,10):
        matrixcell = driver.find_element_by_xpath("//*[@id='game']/table/tbody/tr["+str(row)+"]/td["+str(cell)+"]")
        cellvar = matrixcell.get_attribute("class")
        if cellvar == "game-cell":
            empty_base[row-1,cell-1] = 0
        else:
            paths = matrixcell.find_elements_by_css_selector("path")
            for path in paths:
                value = path.get_attribute("d") 
            for keys, values in vectordic.items():
                if values == value:
                    empty_base[row-1,cell-1] = keys
                    value = ""

print(empty_base)

