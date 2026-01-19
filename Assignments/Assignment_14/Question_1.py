square = lambda x : x * x

def main():
    SQR = 0

    num = int(input("Enter the number :"))

    SQR = square(num)

    print(f"The square of {num} is :",SQR)

if __name__ == "__main__":
    main()