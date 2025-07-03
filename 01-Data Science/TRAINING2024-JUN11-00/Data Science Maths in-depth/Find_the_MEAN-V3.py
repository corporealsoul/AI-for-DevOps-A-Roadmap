import numpy
import pandas

DataSet = pandas.read_csv("TitanicDataSet.csv")

First3Lines = DataSet.head(3)
print("First 3 lines of the dataset:\n", First3Lines)

AllAges = DataSet["Age"]
print("All ages of passengers:\n", AllAges)

AverageAge = DataSet["Age"].mean()
print("Average Age of passengers:", AverageAge)

numpyAges = numpy.mean(DataSet["Age"])
print("Average Age of passengers using numpy:", numpyAges)