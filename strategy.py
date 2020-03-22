import numpy as np
#from launch import output
import sys
# load given sudoku field and rename it to rows
rows = np.load('example.npy')
memorycell = 0
previous = 1
# manipulate given matrix so that columns are in rows
columns = np.rot90(rows)
columns = np.flip(columns, 0)

# outputs 3x3 sudoku fields in rows from given 9x9 sudoku matrix
tempfield = np.array([])
temp = 0
for x in range(0,9,3):
     y = x + 3
     for i in range(1,4):
         temp = i * 3
         i = temp - 3
         tempfield = np.append(tempfield,rows[x:y, i:temp])
                                                         
fields = np.reshape(tempfield,(9,9))



def newmatrix(number,row,column):
    
    global rows
    global columns
    global fields
    rows[row][column] = number
    columns = np.rot90(rows)
    columns = np.flip(columns, 0)
    tempfield = np.array([])
    temp = 0
    for x in range(0,9,3):
        y = x + 3
        for i in range(1,4):
            temp = i * 3
            i = temp - 3
            tempfield = np.append(tempfield,rows[x:y, i:temp])
                                                         
    fields = np.reshape(tempfield,(9,9))


def rowcheck(number,row):
    """
    checks if given int is in the selected row

    """
    return number in rows[row]

def columncheck(number,column):
    """
    checks if given int is in the selected column

    """
    return number in columns[column]

def fieldcheck(number,row,column):
    """
    checks if given int is in the selected field

    """
    sectormatrix = ([0,1,2],
                    [3,4,5],
                    [6,7,8])
    
    counter = -1
    sectorcounter = -1
    for i in range(3,10,3):
        counter += 1
        if row < i:
            for j in range(3,10,3):
                sectorcounter += 1
                if column < j:
                    return number in fields[sectormatrix[counter][sectorcounter]]
                

        
def remember(row,column,minejums):
    global memoryrow
    global memorycol
    global memorycell
    memoryrow = row
    memorycol = column
    memorycell = minejums
        
def mistakechecker(number,row,column):
    if rowcheck(number,row) == False and columncheck(number,column) == False and fieldcheck(number,row,column) == False:
        return True
    return False

def guessingalgo(row,col):
    global rows
    for guess in range(1,10):
        if guess == memorycell:
            continue
        if mistakechecker(guess,row,col):
            remember(row,col,guess)
            newmatrix(guess,row,col)
            print(rows)
            print("")            
        if rows[row][col] == guess:
            atmina = 0
            break
        if guess == 9 and rows[row][col] != 9:
            rows[memoryrow][memorycol] = 0
            print(rows)
            return False
"""

def solve(rows):
    rowcounter = -1
    columncounter = -1                 
    for selectedrow in rows:
        rowcounter += 1
        for selectedcell in selectedrow:
            columncounter += 1
            if selectedcell == 0:
                guessingalgo(rowcounter, columncounter)
            
        columncounter = -1


            
solve(rows)

"""
counter = 4


rowcounter = -1
columncounter = -1                 
for selectedrow in rows:
    rowcounter += 1

    for selectedcell in selectedrow:
        columncounter += 1
            
        if selectedcell == 0:
            if guessingalgo(rowcounter, columncounter) == False:
                sys.exit()
                break

            
    columncounter = -1


                
   