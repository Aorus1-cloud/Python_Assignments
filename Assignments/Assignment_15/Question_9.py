from functools import reduce

def main():
    res = 0
    Data = []

    print("Enter 5 numbers :")
    for i in range(5):
        x = int(input())
        Data.append(x)

    res = reduce(lambda x , y : x * y ,Data)

    print("The product of all elements is :",res)
    
if __name__ == "__main__":
    main()