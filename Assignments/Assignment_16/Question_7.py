def div_by_5(No):
    return No % 5 == 0

def main():
    result = False

    num = int(input("Enter the number :"))

    result = div_by_5(num)

    print("Number divisible by 5 :",result)

if __name__ == "__main__":
    main()