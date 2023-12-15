def swap_case(s):
    s2 = "".join([x.upper() if x.islower() else x.lower() for x in s])
    #Can also use swapcase 
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)