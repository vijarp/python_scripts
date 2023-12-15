#Capitalize first letter of each word

def solve(s):
    s2 = s.split(" ")
    x = " ".join(map(lambda a:a.capitalize(),s2))
    return x