def setornot(number,n):
    mask=1
    if (n&mask==1) or (n&mask==0):
        if (number&(1<<(n-1))):
            print("set")
        else:
            print("not set")

number=int(input("enter the number"))
n=int(input("enter the bit position"))
setornot(number,n)