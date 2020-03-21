from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import time

t0 = time.time()

f = open("vectorpaths.txt").read().splitlines()
output = np.zeros(shape=(9,9))

#cleaner dict solution possible?
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

driver = webdriver.Chrome()
driver.get("http://www.sudoku.com/easy/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))

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
   
print(output)

t1 = time.time()
total = t1-t0
print(total)