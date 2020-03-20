import selenium as sl



driver = sl.webdriver.Chrome()
driver.get("http://www.sudoku.com")

firstcell = driver.find_element_by_xpath("//tr[td='game-cell']//a[@href]")
firstcell.click()