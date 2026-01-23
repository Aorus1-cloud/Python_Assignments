from threading import Thread

def sum_arr(arr,res):
    add = 0
    for num in arr:
        add = add + num

    res["sum"] = add

def product_arr(arr,res):
    prod = 1
    for num in arr:
        prod = prod * num

    res["product"]=prod

def main():
    result = {}
    data = []
    elements = 0 

    elements = int(input("Enter the number of elements :"))

    print("Enter the numbers :")
    for i in range(elements):
        data.append(int(input()))
    
    t1 = Thread(target=sum_arr,args=(data,result))
    t2 = Thread(target=product_arr,args=(data,result))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("The sum of all elements is :",result["sum"])
    print("The product of all elements is :",result["product"])

if __name__ == "__main__":
    main()