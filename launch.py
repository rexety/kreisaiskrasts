from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

#open browser & wait until loaded
driver = webdriver.Chrome()
driver.get("http://www.sudoku.com/hard/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))


#read table into an ndarray
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
   
#print(output)

##solve with function from the strategy file --- HOW IT SHOULD WORK
#import strategy
#solve(output) 


# #input
# newgame = driver.find_element_by_class_name("game-cell")
# newgame.click()
# newgame.send_keys(Keys.ARROW_DOWN)


t1 = time.time()
total = t1-t0
#print(total)