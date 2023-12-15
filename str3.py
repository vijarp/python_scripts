def mutate_string(string, position, character):
    return string[:position]+character+string[(position+1):]
    #Also can convert to list and join back
    """
    l1 = list(string)
    l1[position] = character
    return "".join(l1)
    """

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)