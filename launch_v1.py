from selenium import webdriver
#from selenium import webdriverwait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.sudoku.com")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'game')))

#driver.implicitly_wait(10)
firstcell = driver.find_element_by_xpath('/html/body/header/div/div[3]/div[1]')[0]
firstcell.click()

