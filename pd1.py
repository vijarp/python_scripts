import pandas as pd 

data = pd.read_csv('datasets/tweets.csv')

# Print the head of the data data
print(data.head())

# Print information about data
print(data.info())

# Print the shape of data
print(data.shape)

# Print a description of data
print(data.describe())