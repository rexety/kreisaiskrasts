import numpy as np


hints = np.load('example_v1.npy')

randomized_game = np.zeros(shape=(9,9))


def fill(array):
    
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == 0:
                randomized_game[i,j] = np.random.randint(low = 1, high = 9)
            else:
                randomized_game[i,j] = hints[i,j]
                
    return randomized_game


fill(hints)

# def errors(array):
    
#     for row in array:
        
    
    
#def randomize errors


print("Before:")
print(hints)

print("After:")
print(randomized_game)
