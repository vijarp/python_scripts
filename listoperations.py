
if __name__ == '__main__':
    list1=[]
    

    def performoperations(comm,*par):
        global list1
        
        if comm == "print":
            print(list1)
        elif comm == "append":
            val = int(list(par)[0])
            list1.append(val)
        elif comm == "insert":
            para = list(par)
            index1 = int(para[0])
            el = int(para[1])
            list1.insert(index1,el)
        elif comm == "sort":
            list1.sort()
        elif comm == "pop":
            list1.pop() 
        elif comm == "reverse":
            list1.reverse() 
        elif comm == "remove":
            val = int(list(par)[0])
            list1.remove(val)
        else:
            print("Invalid Command")  
        
    N = int(input())
    for i in range(N):
        comm,*par = input().strip().split(" ")
        performoperations(comm,*par)

    