def oneoddoccuring(arr):
    res=0
    for element in arr:
        res=res^element
    return res

arr=[]
n=int(input("enter the array size"))
while(n):
    num=int(input("enter the number"))
    arr.append(num)
    n-=1

print("odd occuring element is ",oneoddoccuring(arr))
