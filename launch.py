from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np

empty_base = np.zeros(shape=(9,9))
print(empty_base)


driver = webdriver.Chrome()
driver.get("http://www.sudoku.com/easy/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))

newgame = driver.find_element_by_class_name("game-cell")
#newgame.click()

#enters number 1 in the first cell through given numpad

#one = driver.find_element_by_class_name("numpad-item")
#one.click()
    
#through dynamic xpath iterate over whole 9x9 matrix, if empty put zero else read vector path

for row in range(1,10):
    for cell in range(1,10):
        matrixcell = driver.find_element_by_xpath("//*[@id='game']/table/tbody/tr["+str(row)+"]/td["+str(cell)+"]")
        cellvar = matrixcell.get_attribute("class")
        if cellvar == "game-cell":
            empty_base[row-1,cell-1] = 0
        else:
            empty_base[row-1,cell-1] = 1
            paths = matrixcell.find_elements_by_css_selector("path")
            for path in paths:
                #nomainot fill uz d iegūsti path vektorus, kurus var salīdzināt ar dictionary 
                value = path.get_attribute("fill") 
            print(value)
  
print(empty_base)