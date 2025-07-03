import matplotlib.pyplot
import numpy
import pandas
import matplotlib
import seaborn

DataSet = pandas.read_csv("TitanicDataSet.csv")

# medianAge = numpy.median(DataSet["Age"])
# print("Median Age:", medianAge)


# nullData = DataSet.isnull().sum()
# print("Null Data:", nullData)


# DataSet["Age"] = DataSet["Age"].fillna(DataSet["Age"].median())
# DataSet["Age"] = DataSet["Age"].fillna(DataSet["Age"].mean())

# median_age = DataSet["Age"].median()
# mean_age = DataSet["Age"].mean()

# print("Median Age:", median_age)
# print("Mean Age:", mean_age)



DataSet["Fare"] = DataSet[]