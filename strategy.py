import numpy as np
from launch_v1 import output
import sys
# load given sudoku field and rename it to rows


# rows = np.load('example.npy')
rows = output

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


def rowcheck(number,row):

    return number in rows[row]



def columncheck(number,column):

    return number in columns[column]



def fieldcheck(number,row,column):

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
                


def mistakechecker(number,row,column):
    if rowcheck(number,row) == False and columncheck(number,column) == False and fieldcheck(number,row,column) == False:
        return True
    return False


def searchzero(matrix):
    for row in range(len(matrix)):
        for cell in range(len(matrix)):
            if matrix[row][cell] == 0:
                return row,cell
    print(" ")
    print(" ")
    print(rows)
    sys.exit()
    
def guessing(matrix):                
    search = searchzero(matrix)
    row = search[0]
    cell = search[1]
    for guess in range(1,10):
        if mistakechecker(guess,row,cell) == True:
            matrix[row][cell] = guess
            if guessing(matrix):
                return
            else:
                matrix[row][cell] = 0
            
            

guessing(rows)