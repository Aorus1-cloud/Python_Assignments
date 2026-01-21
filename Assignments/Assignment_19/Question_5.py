from functools import reduce 
from math import sqrt

def prime(No):
    if No == 1:
        return False
    
    elif No == 2:
        return True
    
    for i in range(2,int(sqrt(No))+1):
        if No % i == 0 :
            return False
        
    return True

def double(No):
    return No * 2

def max(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2


def main():
    data = list()

    elements = int(input("Enter number of elements :"))

    print("Enter numbers :")
    for i in range(elements):
        data.append(int(input()))

    print("Input List =",data)

    # filter
    fdata = list(filter(prime,data))

    print("Filter list =",fdata)
    # map
    mdata = list(map(double,fdata))

    print("Map list =",mdata)
    # reduce
    rdata = reduce(max,mdata)

    print("Reduced Output =",rdata)
    
if __name__ == "__main__":
    main()