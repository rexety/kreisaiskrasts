import numpy as np


hints = np.load('example_v1.npy')


def fill_randomly(hints):
    
    random_game = np.zeros(shape=(9,9))
    
    for i, row in enumerate(hints):
        for j, cell in enumerate(row):
            if cell == 0:
                # random_game[i,j] = np.random.randint(low = 1, high = 9)
                random_game[i,j] = 1
            else:
                random_game[i,j] = hints[i,j]
                
    return random_game

random_game = fill_randomly(hints)


def rows(sudoku):
    
    rows = sudoku
    return rows
    

def cols(sudoku):
    
    rows = sudoku
    columns = np.rot90(rows)
    columns = np.flip(columns, 0)
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


random_rows = rows(random_game)
random_cols = cols(random_game)
random_sects = sects(random_game)

hint_rows = rows(hints)
hint_cols = cols(hints)
hint_sects = sects(hints)

negative_rows = -random_rows + 2 * hint_rows
negative_cols = -random_cols + 2 * hint_cols
negative_sects = -random_sects + 2 * hint_sects

print(negative_rows)
print("")


def remove_row_errors():

    rowfix = np.zeros(shape=(9,9))
    
    for n in range(9):
        rowfix[n] = np.around([0 if -i in hint_rows[n] else i for i in negative_rows[n]])
        
     #   rowfix[n] = [0 if np.count_nonzero(-rowfix[n] == n+1) > 1 else i for i in rowfix[n]]

    return rowfix


def remove_col_errors():
    
    fixed_rows = remove_row_errors()
    colfix = cols(fixed_rows)
    
    for n in range(9):
        colfix[n] = np.around([0 if -i in hint_cols[n] else i for i in colfix[n]])

    return colfix.T


def remove_sect_errors():
    
    fixed_rowcols = remove_col_errors()
    sectfix = sects(fixed_rowcols)

    for n in range(9):
        sectfix[n] = np.around([0 if -i in hint_sects[n] else i for i in sectfix[n]])
        
    return sectfix


asd = remove_col_errors()

print(asd)
