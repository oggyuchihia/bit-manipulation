def powerset(set,size):
    powersetsize=2**size
    outer=0
    inner=0
    for outer in range(0,powersetsize):
        for inner in range(0,size):
            if (outer&(1<<inner)>0):
                print(set[inner],end="")
        print("")

size=int(input("enter the set size"))
set=[]
for i in range(0,size):
    x=int(input("enter the element"))
    set.append(x)

powerset(set,size)