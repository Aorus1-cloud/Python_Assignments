def Cube(Num):
    return Num ** 3


def main():
    Result = 0

    Number = int(input("Enter the Number : "))

    Result = Cube(Number)

    print("The Cube is :",Result)

if __name__ == "__main__":
    main()