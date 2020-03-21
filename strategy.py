import numpy as np
#from launch import output

#function row number does not match
#function column number does not match
#function field does not match
example = np.load('example.npy')
rows = example


columns = np.rot90(example)
columns = np.flip(columns, 0)


tempfield = np.array([])

temp = 0
for x in range(0,9,3):
     y = x + 3
     for i in range(1,4):
         temp = i * 3
         i = temp - 3
         tempfield = np.append(tempfield,example[x:y, i:temp])
                                                         
fields = np.reshape(tempfield,(9,9))
  
"""
we got 3 arrays - row, column, fields


start row, if other than 0 use that cell
when cell picked check if the row and columnd does
not have a matching number

"""


def rowcheck(number,row):
    """
    pohuj

    """
    return number in rows[row]

def columncheck(number,column):
    """
    pohuj

    """
    return number in columns[column]

def fieldcheck(number,field):
    """
    gl bleg
    """



print(columncheck(2, 2))



rowy = -1
coly = -1

for rowx in example:
    rowy += 1
    for cellx in rowx:
        coly += 1
        if cellx == 0:
            for i in range(1,9):
                if rowcheck(i,rowy) == True and columncheck(i,coly) == True:
                    print("wat")
                coly = -1
               
                
"""
get fieldcheck working
if int can be used put it into the big matrix
what if the whole range is not usable and backtracking has to be used
"""
                