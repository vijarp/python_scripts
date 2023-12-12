
"""Project to analyzt if netflix movies are getting shorter"""

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
netflix_df = pd.read_csv("datasets/netflix_data.csv")

#Checking Total Rows
print(netflix_df.shape)

#Filtering TV Shows and removing them
netflix_subset = netflix_df[netflix_df["type"] != "TV Show"]

#Checking Shape to find rows
print(netflix_subset.shape)

print(netflix_subset.head())


#Removing unnecessary rows
netflix_movies = netflix_subset[["title","country","genre","release_year","duration"]]

#short Movies analysis
short_movies = netflix_movies[netflix_movies["duration"] < 60]


#Describe to analyze and have more info
print(netflix_movies.describe())

print(short_movies.describe())


#Colors for different Genre
colors = []
for g in netflix_movies["genre"]:
    if g == "Children":
        colors.append("red")
    elif g=="Documentaries":
        colors.append("blue")
    elif g=="Stand-Up":
        colors.append("green")
    else:
        colors.append("yellow")


#Plotting it to check 
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies["release_year"],netflix_movies["duration"],c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()



#Some clusters are there at the bottom but we can also see big lines at top - so we cannot say for sure if length is decreasing
answer = "maybe"
# Start coding!