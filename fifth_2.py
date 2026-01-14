def sumation(n):
    
    if(n==0):
        return 0
    
    return sumation(n-1)+n

sum = sumation(5)

print(sum)