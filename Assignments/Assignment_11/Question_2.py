def NumCount(No):
    Res = 0

    for Num in No:
        Res += 1

    return (Res)


def main():
    Result = 0

    Number = input("Enter the Number : ")

    Result = NumCount(Number)

    print(f"The digits in {Number} are :",Result)

if __name__ == "__main__":
    main()