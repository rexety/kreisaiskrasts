import numpy as np

hints = np.load('example_v1.npy')
solution = hints.copy()

print(hints)
print("")

def rows(sudoku):
    
    rows = sudoku
    return rows
    

def cols(sudoku):
    
    columns = sudoku.T
    return columns


def sects(sudoku): 
    
    tempfield = np.array([])
    temp = 0
    for x in range(0,9,3):
          y = x + 3
          for i in range(1,4):
              temp = i * 3
              i = temp - 3
              tempfield = np.append(tempfield, sudoku[x:y, i:temp])
                                                             
    sectors = np.reshape(tempfield,(9,9))
    
    return sectors


def fixed_rows(sudoku):

    for n in range(9):
        rows(sudoku)[n] = np.around([0 if -i in rows(hints)[n] else i for i in rows(sudoku)[n]])
        rows(sudoku)[n] = [0 if np.count_nonzero(rows(sudoku)[n] == i) > 1 else i for i in rows(sudoku)[n]]
        
    return sudoku

      
def fixed_cols(sudoku):

    for n in range(9):
        cols(sudoku)[n] = np.around([0 if -i in cols(hints)[n] else i for i in cols(sudoku)[n]])
        cols(sudoku)[n] = [0 if np.count_nonzero(cols(sudoku)[n] == i) > 1 else i for i in cols(sudoku)[n]]

    return sudoku


def fixed_sects(sudoku):
    
    hintz = sects(hints).copy()
    solutionz = sects(sudoku).copy()
    
    for n in range(9):
        solutionz[n] = np.around([0 if -i in hintz[n] else i for i in solutionz[n]])
        solutionz[n] = [0 if np.count_nonzero(solutionz[n] == i) > 1 else i for i in solutionz[n]]

    return solutionz


# print(sects(fixed_sects(fixed_rows(fixed_cols(solution)))))


def fill(sudoku):
    
    # for n in range(1,10):
        while np.count_nonzero(abs(sudoku) == 9) != 9:
        
            for i, row in enumerate(sudoku):
                for j, cell in enumerate(row):
                    if cell == 0:
                        sudoku[i,j] = np.random.randint(low =-9, high = -1)
                    else:
                        # sudoku[i,j] = sects(fixed_sects(fixed_rows(fixed_cols(sudoku))))[i,j]
                        sudoku = sects(fixed_sects(fixed_rows(fixed_cols(sudoku))))
                        
            # 
            
            print(abs(sudoku))
            
        return abs(sudoku)

print(fill(solution))

'''
ideas:
    
    
if not in row:
    if not in col:
        if not in sect:
            enter number
        else remove duplicates
    else remove duplicates
else remove duplicates
            
'''    

# def cellvalue(sudoku, row, col):
    
#     value = int(sudoku[row][col])
    
#     if row <3:
#         if col <3:
#             sect = 1
#         elif col >5:
#             sect = 3
#         else:
#             sect = 2
    
#     elif row >5:
#         if col <3:
#             sect = 7
#         elif col >5:
#             sect = 9
#         else:
#             sect = 8
            
#     else:
#         if col <3:
#             sect = 4
#         elif col >5:
#             sect = 6
#         else:
#             sect = 5
            
    
#     return value, row, col, sect