# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
if __name__ == '__main__':
    t = input().strip().split(" ")
    s1 = int(t[1])
    l1 = []
    for i in range(int(t[0])):
        input1= [int(x)*int(x) for x in input().strip().split(" ")]
        input1.pop(0)
        set1 = set(input1)
        l1.append(set1)
    print(l1)
    sum1 = [sum(x) % s1 for x in product(*l1)]
    print(sum1)
    print(max(sum1))


