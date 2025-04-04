def evenodd(n):
    if (n^1==n+1):
        return True
    else:
        return False
    
n=int(input("Please enter a number"))
if evenodd(n):
    print("number is even")

else:
    print("the number is odd")