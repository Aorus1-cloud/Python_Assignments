def SumDigits(No):
    res = 0 

    for num in No:
        res = res + int(num)

    return(res)


def main():
    result = 0
    
    number = input("Enter the number :")

    result = SumDigits(number)

    print(f"The addition of the digits in the {number} is :",result)


if __name__ == "__main__":
    main()
