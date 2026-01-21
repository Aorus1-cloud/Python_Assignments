def ChkNum(No):
    if No > 0 :
        return("Positive")
    elif No < 0:
        return("Negative")
    else:
        return("Zero")


def main():
    result = str()

    num = int(input("Enter the number :"))

    result = ChkNum(num)

    print(f"The number is {result}.")

if __name__ == "__main__":
    main()