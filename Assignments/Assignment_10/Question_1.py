def table(Num):
    Result = list()
    for i in range(1,11):
        Ans = 0
        Ans = Num * i  
        Result.append(Ans)
    
    return Result

def main():
    Number = int(input("Enter the Number : "))

    Res = table(Number)
    for num in Res:
        print(num)

if __name__ == "__main__":
    main()