import numpy as np


#load the hint array and an empty one for random numbers
hints = np.load('example_v1.npy')
randomized_game = np.zeros(shape=(9,9))

#fill empty spaces with random numbers
def fill_randomly(array):
    
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == 0:
                randomized_game[i,j] = np.random.randint(low = 1, high = 9)
            else:
                randomized_game[i,j] = hints[i,j]
                
    return randomized_game

fill_randomly(hints)


#define rows, columns and squares
rows = randomized_game

columns = np.rot90(rows)
columns = np.flip(columns, 0)

tempfield = np.array([])
temp = 0
for x in range(0,9,3):
      y = x + 3
      for i in range(1,4):
          temp = i * 3
          i = temp - 3
          tempfield = np.append(tempfield,randomized_game[x:y, i:temp])
                                                         
fields = np.reshape(tempfield,(9,9))

#filter hints - make them the only positive values --- pagaidaam tikai pirmaa rinda lai nepistu galvu
negatives = -randomized_game[0] + 2 * hints[0]

print(negatives)

#delete duplicates if hint exists --- IN PROGRESS
for n in range(10):
    
    # if n in negatives:
        # new_items = np.where(negatives == -n, 0, negatives) #straadaa tikai jaunaakajam iterationam
        
        new_items = [-n if -n in negatives else n for n in negatives] #straadaa tikai ja visi/abi skaitlji ir rindaa asdejnahujble
        
        # new_items = [0 if n in negatives else n for n in negatives]

print(new_items)


#
# structure
#


# def find_errors(array):
    
#     for row in rows:
#         if
        
    
    
#def randomize errors():
        # asd




