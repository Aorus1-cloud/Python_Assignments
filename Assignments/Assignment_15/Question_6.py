from functools import reduce
def main():
    result = []
    Data = []

    print("Enter 5 numbers :")
    for i in range(5):
        x = int(input())
        Data.append(x)

    result = reduce(lambda x , y : x if  x < y else y ,Data)

    print("The smallest of all given numbers is :",result)

if __name__ == "__main__":
    main()
