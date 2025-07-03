import matplotlib.pyplot
import numpy
import pandas
import matplotlib
import seaborn

DataSet = pandas.read_csv("TitanicDataSet.csv")

# seaborn.histplot(x="Age", data=DataSet, kde=True)
# matplotlib.pyplot.xlabel("Passenger Age (in years)")
# matplotlib.pyplot.ylabel("Number of Passengers")
# matplotlib.pyplot.title("Distribution of Passenger Ages on Titanic")
# matplotlib.pyplot.show()


# seaborn.histplot(x="Age", data=DataSet, bins=[i for i in range(0, 100, 10)], kde=True)
# matplotlib.pyplot.xlabel("Passenger Age (in years)")
# matplotlib.pyplot.ylabel("Number of Passengers")
# matplotlib.pyplot.title("Distribution of Passenger Ages on Titanic")
# matplotlib.pyplot.show()


# mean_age = numpy.mean(DataSet["Age"])
# seaborn.histplot(x="Age", data=DataSet, kde=True, bins=[loop for loop in range(0, 100, 10)])
# matplotlib.pyplot.plot([mean_age for loop in range(0, 300)],[loop for loop in range(0, 300)])
# matplotlib.pyplot.xlabel("Passenger Age (in years)")
# matplotlib.pyplot.ylabel("Number of Passengers")
# matplotlib.pyplot.title("Distribution of Passenger Ages on Titanic")
# matplotlib.pyplot.show()


# mean_age = numpy.mean(DataSet["Age"])
# seaborn.histplot(x="Age", data=DataSet, bins=[loop for loop in range(0, 100, 10)], kde=True)
# matplotlib.pyplot.axvline(mean_age, color='red', linestyle='--', linewidth=2, label=f"Mean Age = {mean_age:.1f}")
# matplotlib.pyplot.xlabel("Passenger Age (in years)")
# matplotlib.pyplot.ylabel("Number of Passengers")
# matplotlib.pyplot.title("Distribution of Passenger Ages on Titanic")
# matplotlib.pyplot.show()