def factors(No):
    factor = list()

    for i in range(1,No+1):
        if No % i == 0:
            factor.append(i)

    return factor

        

def main():
    result = list()

    number = int(input("Enter the number :"))

    result = factors(number)

    print(f"The factors of {number} are :",result)


if __name__ == "__main__":
    main()