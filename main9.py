def power4(n):
    return n>0 and (n & (n-1))==0 and (n-1)%3==0

n=int(input("enter the number"))
if power4(n):
    print("number is a power of 4")

else:
     print("number is not a power of 4")