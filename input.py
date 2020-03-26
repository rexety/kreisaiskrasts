from launch import output
from launch import driver
from strategy import guessing


guessing(output)
print(" ")
print("Solved")
print(" ")
print(output)



def move_to_cell(row,column):
    move = driver.find_element_by_xpath(f'//*[@id="game"]/table/tbody/tr[{row}]/td[{column}]')
    move.click()

def input_number(number):
    
    numpaditem = driver.find_element_by_xpath(f'//*[@id="sudoku-wrapper"]/div[2]/div[2]/nav/div[2]/div/div[{number}]')
    numpaditem.click()
    

def fill():
    for row in range(0,len(output)):
        for column in range(0,len(output)):
            move_to_cell(row+1,column+1)
            input_number(output[row][column])
    print(" ")        
    return print("done")

fill()