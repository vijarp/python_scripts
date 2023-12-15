#sort by second lowest - all occurences
import time
a=[]
b=set()

""" for _ in range(int(input())):
    name=input()
    score=float(input())
    a.append([name,score])
    b.add(score) """
a = [("A",92),("D",22),("C",13),("B",22),("E",62)]
b = {92,22,13,62}
b = list(b)
b.sort()
l1 = [el[0] for el in a if el[1] == b[1]]
l1.sort()
for el in l1:
    print(el)
