def ChkNum(No):
    return No % 2 == 0


def main():
    result = False 

    num = int(input("Enter your number :"))

    result = ChkNum(num)

    if result:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()