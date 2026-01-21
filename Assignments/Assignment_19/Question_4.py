from functools import reduce 

def even_list(No):
    return No % 2 == 0

def sqr_list(No):
    return No ** 2

def sum_list(No1,No2):
    return No1 + No2

def main():
    data = list()

    elements = int(input("Enter number of elements :"))

    print("Enter numbers :")
    for i in range(elements):
        data.append(int(input()))

    print("Input List =",data)

    # filter
    fdata = list(filter(even_list,data))

    print("Filter list =",fdata)
    # map
    mdata = list(map(sqr_list,fdata))

    print("Map list =",mdata)
    # reduce
    rdata = reduce(sum_list,mdata)

    print("Reduced Output =",rdata)
    
if __name__ == "__main__":
    main()