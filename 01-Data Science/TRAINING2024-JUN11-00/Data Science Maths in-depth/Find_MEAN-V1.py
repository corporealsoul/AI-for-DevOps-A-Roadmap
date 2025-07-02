import numpy as np
import pandas as pd

ar = np.array([1, 2, 3, 4, 5])

sum_of_data = np.sum(ar)
num_of_elements = ar.size
length_of_array = len(ar)

print("Sum of data:", sum_of_data)
print("Number of elements:", num_of_elements)
print("Length of array:", length_of_array)

mean = sum_of_data / num_of_elements
print("Mean of data:", mean)

