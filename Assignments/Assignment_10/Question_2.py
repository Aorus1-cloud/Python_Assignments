def SumN(No):
    Result = 0

    for i in range(1,No+1):
        
        Result = Result + i

    return Result


def main():
    Res = 0 

    Num = int(input("Enter the Number : "))

    Res = SumN(Num)

    print("The sum is : ",Res)


if __name__ == "__main__":
    main()