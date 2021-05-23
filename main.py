def primenumberchecker(n):
    count = 0
    for i in range(1,n+1):
        rem = n%i
        if rem == 0:
            count = count + 1
            
    if count == 2:
        return f"{n} is a Prime Number"
    else:
        return f"{n} is not a Prime Number"
n = int(input())
print(primenumberchecker(n))
