import numpy as np

example = np.load('example_v1.npy')


def fill(array):
    
    for i, r in enumerate(array):
        for j, c in enumerate(r):
            if c == 0:
                array[i,j] = np.random.randint(low = 1, high = 9)
                
    return array
    

random_array = fill(example)

print("Before:")
print(example)

print("After:")
print(random_array)
