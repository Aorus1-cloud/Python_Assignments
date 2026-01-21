def main():
    result = 0 

    num = int(input("Enter the number :"))

    power = lambda x : x ** 2

    result = power(num)

    print(f"The power of {num} is :",result)

if __name__ == "__main__":
    main()