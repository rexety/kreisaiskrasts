import numpy as np
#from launch import output
import sys
# load given sudoku field and rename it to rows
rows = np.load('example.npy')


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



print(rows)
print(columns)
print(fields)


rows[1][1] = 9
rows[7][7] = 7

print(rows)
print(columns)
print(fields)





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
                
"""
                
depth = 0
memoryrow = [-1]
memorycol = [-1]
memorycell = [-1]
def remember(row,column,minejums):
    global memoryrow
    global memorycol
    global memorycell
    global depth
    depth = 0
    memoryrow.append(row)
    memorycol.append(column)
    memorycell.append(minejums)
"""        
def mistakechecker(number,row,column):
    if rowcheck(number,row) == False and columncheck(number,column) == False and fieldcheck(number,row,column) == False:
        return True
    return False
"""
def guessingalgo(row,col):
    global depth
    global rows
    if counter == 0:
        sys.exit()
    for guess in range(1,10):
        if guess == memorycell[-1-depth]:
            continue
        if mistakechecker(guess,row,col):
            remember(row,col,guess)
            newmatrix(guess,row,col)
            print(rows)
            print("")
            depth = 0
            
        if rows[row][col] == guess:
            break
        if guess == 9 and rows[row][col] != 9:
            depth += 1
            rows[memoryrow[-1-depth]][memorycol[-1-depth]] = 0
            solve(rows)



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

counter = 500

def solve(rowX):
    
    global rowcounter
    global columncounter
    global counter
    counter -= 1
    if counter == 0:
        sys.exit()
    rowcounter = -1
    columncounter = -1                 
    for selectedrow in rowX:
        rowcounter += 1
    
        for selectedcell in selectedrow:
            columncounter += 1
                
            if selectedcell == 0:
                guessingalgo(rowcounter, columncounter)
    
    
                
        columncounter = -1

solve(rows)

"""
def searchzero(matrix):
    rowloc = -1
    colloc = -1
    for rows in matrix:
        rowloc += 1
        for cell in rows:
            colloc += 1
            if cell == 0:
                return  rowloc,colloc
            
            
            
            
#def guessing(row,col):
    