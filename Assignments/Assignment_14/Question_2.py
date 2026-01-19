cube = lambda x : x**3

def main():
    result = 0 

    num = int(input("Enter the number :"))

    result = cube(num)

    print(f"The cube of {num} is :",result)

if __name__ == "__main__":
    main()