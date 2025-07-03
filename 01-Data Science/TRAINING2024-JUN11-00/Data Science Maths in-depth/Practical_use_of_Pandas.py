import pandas

DataSet = pandas.read_csv("TitanicDataSet.csv")

# print("Dataset :", DataSet)
# print(DataSet.isnull().sum())

children = DataSet[DataSet["Age"] < 12]
print("Children in the dataset: \n", children[["Name", "Age"]])