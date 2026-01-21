from functools import reduce 

def in_btw_70_90(No):
    return No >= 70 and No <= 90

def add_10(No):
    return No + 10

def product(No1,No2):
    return No1 * No2

def main():
    data = list()

    elements = int(input("Enter number of elements :"))

    print("Enter numbers :")
    for i in range(elements):
        data.append(int(input()))

    print("Input List =",data)

    # filter
    fdata = list(filter(in_btw_70_90,data))

    print("Filter list =",fdata)
    # map
    mdata = list(map(add_10,fdata))

    print("Map list =",mdata)
    # reduce
    rdata = reduce(product,mdata)

    print("Reduced Output =",rdata)
    
if __name__ == "__main__":
    main()