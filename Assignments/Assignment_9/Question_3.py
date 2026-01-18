def Sqr(Num):
    return Num ** 2

def main():
    Result = 0 

    Number= int(input("Enter the Number : "))

    Result = Sqr(Number)

    print("The Square is : ",Result)

if __name__ == "__main__":
    main()