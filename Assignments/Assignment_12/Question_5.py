def reversecounting(No):
    Result = list()

    for i in range(No,0,-1):
        Result.append(i)

    return Result
 
def main():
    Res = list()

    num = int(input("Enter the number :"))

    Res = reversecounting(num)

    print(f"The reverse counting till {num} is : {Res}")

if __name__ == "__main__":
    main()