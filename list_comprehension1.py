import pandas as pd

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [ [col for col in range(0,5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)


#Conditional comprehension
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member)>=7]

# Print the new list
print(new_fellowship)



#IF Else = use if before for

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member  if len(member)>=7 else "" for member in fellowship]

# Print the new list
print(new_fellowship)


df = pd.read_csv("datasets/tweets.csv")


#Extract time from csv file tweets.csv and field created_at using comprehension

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]


#With if condition

# Extract the created_at column from df: tweet_time
tweet_time = df["created_at"]

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)




#Chess Squares using comprehension

chess1 = [ chr(i+97) + "" + str(j) for i in range(8) for j in range(8)]
print(chess1)
#As double dimension array
chess2 = [[ chr(i+97) + str(j+1) for j in range(8)] for i in range(8)]
print(chess2)
"""Output
>>> [[ chr(i+97) + str(j+1) for j in range(8)] for i in range(8)]
[['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
 ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
   ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], 
   ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'], 
   ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'], 
   ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'], 
   ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'], 
   ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']]
"""

# Print the extracted times
print(tweet_clock_time)
