import numpy as np
#from launch import output

# load given sudoku field and rename it to rows
example = np.load('example.npy')
rows = example

# manipulate given matrix so that columns are in rows
columns = np.rot90(example)
columns = np.flip(columns, 0)




# outputs 3x3 sudoku fields in rows from given 9x9 sudoku matrix
tempfield = np.array([])
temp = 0
for x in range(0,9,3):
     y = x + 3
     for i in range(1,4):
         temp = i * 3
         i = temp - 3
         tempfield = np.append(tempfield,example[x:y, i:temp])
                                                         
fields = np.reshape(tempfield,(9,9))



print(rows)
print(columns)
print(fields)



"""
we got 3 arrays - row, column, fields


start row, if other than 0 use that cell
when cell picked check if the row and columnd does
not have a matching number

"""


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

def fieldcheck(number,field):
    """
    checks if given int is in the selected field
    """






rowy = -1 # counts which row it is with an int
coly = -1 # counts which column it is with an int
for rowx in example:
    rowy += 1
    for cellx in rowx:
        coly += 1
        if cellx == 0:
            for i in range(1,9):
                if rowcheck(i,rowy) == True and columncheck(i,coly) == True: #checks if int can be used in the free space according to sudoku rules
                    break#print("wat")
                coly = -1
               
                
"""
TO DO
get fieldcheck working
if int can be used put it into the big matrix
what if the whole range is not usable and backtracking has to be used
"""
                