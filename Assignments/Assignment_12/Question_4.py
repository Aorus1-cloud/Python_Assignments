def counting(No):
    Result = list()

    for i in range(1,No+1):
        Result.append(i)

    return Result
 
def main():
    Res = list()

    num = int(input("Enter the number :"))

    Res = counting(num)

    print(f"The counting till {num} is : {Res}")

if __name__ == "__main__":
    main()