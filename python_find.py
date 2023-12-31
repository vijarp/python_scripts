movies = ["137    heck , jackie doesn't even have enough money f","138    in condor , chan plays the same character he's.."]

"""The find() method returns -1 if the substring is not found, while the index() method raises a ValueError exception.
"""

for movie in movies:
    try:
        # Find the first occurrence 
        print(movie.find("money", 12, 51))
    except ValueError:
        print("substring not found")



for movie in movies:
    try:
        # Find the first occurrence of word
        print(movie.index("money", 12, 51))
    except ValueError:
        print("substring not found")
