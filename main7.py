def twoodd(arr,size):
    xor=arr[0]
    x=0
    y=0
    sb=0
    for i in range(1,size):
        xor=xor^arr[i]
    sb=xor&~(xor-1)
    for i in range(size):
        if arr[i]&sb:
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("two odd occuring elemnts are ",x,y)

arr=[]
n=int(input("enter the array size"))
for i in range(0,n):
    num=int(input("enter the number"))
    arr.append(num)
    

twoodd(arr,n)