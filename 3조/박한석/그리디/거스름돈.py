def divisor(n):
    count = [0, 0, 0, 0, 0]
    while n > 0:
        if (n // 500) > 0:
            count[0] = (n//500)
            n = n - (n//500 * 500)
            
        elif (n // 100) > 0:
            count[1] = (n//100)
            n = n - (n//100 * 100)
            
        elif (n // 50) > 0:
            count[2] = (n//50)
            n = n - (n//50 * 50)
            
        else:
            count[3] = (n//10)
            n = n - (n//10 * 10)
            
    print(count)

n = int(input()) # 거스름 돈 
divisor(n)