from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import numpy as np
import time



f = open("vectorpaths.txt").read().splitlines()
output = np.zeros(shape=(9,9))

# Dictionary for numbers in game cell

keys = []
for i in range(1,10):
    keys.append(i)
    
vectordict = dict.fromkeys(keys)

temp = 1
for x in f:
    vectordict[temp] = x
    temp += 1
    if temp == 10:
        break

# Open browser & wait until loaded

driver = webdriver.Chrome()
driver.get("http://www.sudoku.com/medium/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))


# Read table into an ndarray

for row in range(1,10):  
    for cell in range(1,10):     
        web_cells = driver.find_element_by_xpath(f'//*[@id="game"]/table/tbody/tr[{row}]/td[{cell}]')   
        
        if web_cells.get_attribute("class") == "game-cell game-value":
            paths = web_cells.find_elements_by_tag_name("path")
            
            for path in paths:
                web_value = path.get_attribute("d")       
                    
            for keys, values in vectordict.items():
                if values == web_value:
                    output[row-1,cell-1] = keys   
   





