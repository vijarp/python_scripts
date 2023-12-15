if __name__ == '__main__':
    s = input()
    
    #Short Version
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
    
    
    
    
    #Without using any
    
    
    a1 = [x.isalnum() for x in s]
    if True in a1:
        print(True)
    else:
        print(False)
        

    a2 = [x.isalpha() for x in s]
    if True in a2:
        print(True)
    else:
        print(False)
    a3 = [x.isdigit() for x in s]
    if True in a3:
        print(True)
    else:
        print(False)
    a4 = [x.islower() for x in s]
    if True in a4:
        print(True)
    else:
        print(False)
    a5 = [x.isupper() for x in s]
    if True in a5:
        print(True)
    else:
        print(False)
    