#Find no of times substring occurs in string

def count_substring(string, sub_string):
    l2=len(sub_string)
    cnt=0
    for i in range(0,len(string)):
        if string[i:i+l2] == sub_string:
            cnt=cnt+1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)