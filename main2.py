def numofbits(n):
    count=0
    while(n):
        count+=1
        n>>=1
    return count

n=int(input("Enter the number"))

print("total number of bits" ,numofbits(n))