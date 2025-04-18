def swap(x,y):
    x=x^y
    y=y^x
    x=x^y
    print("after swaping=",x,y)

def swap2(a,b):
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print("after swaping=",a,b)

swap(10,20)
swap2(10,20)