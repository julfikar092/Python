def sumation(n):
    sum=0
    if(n==0):
        return 0
    else:
        return(sumation(n-1))

print(sumation(5))