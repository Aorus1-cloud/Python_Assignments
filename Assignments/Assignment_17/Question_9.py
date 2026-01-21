def length(No):
    return len(No)

def main():
    result = 0 

    num = input("Enter the number :")

    result = length(num)

    print(f"The length of {num} is {result}")


if __name__ == "__main__":
    main()