def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1,number+1):
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(str(i).rjust(width) + " " +octal.rjust(width)+ " "+hexa.rjust(width)+" "+bina.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)