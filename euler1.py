import time
if __name__ == '__main__':
    t = int(input().strip())
    t1 = time.time()
    for t_itr in range(t):
        n = int(input().strip())
        #n = int(input().strip())
        
        n -= 1  # Adjust to include numbers less than n
        sum3 = 3 * (n // 3 * (n // 3 + 1)) // 2
        sum5 = 5 * (n // 5 * (n // 5 + 1)) // 2
        sum15 = 15 * (n // 15 * (n // 15 + 1)) // 2
        sum1 = sum3 + sum5 - sum15
        #sum1= sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
        print(sum15,sum5,sum3)
        print(sum1)
    print(time.time() - t1)    