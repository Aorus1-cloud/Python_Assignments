from functools import reduce
def main():
    result = []
    Data = []

    print("Enter 5 numbers :")
    for i in range(5):
        x = int(input())
        Data.append(x)

    result = reduce(lambda x , y : x+y,Data)

    print("The addition of all number is :",result)

if __name__ == "__main__":
    main()
