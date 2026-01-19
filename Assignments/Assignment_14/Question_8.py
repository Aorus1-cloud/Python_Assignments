add = lambda a,b:a+b

def main():
    result = 0

    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    result = add(num1,num2)

    print("The addition is :",result)

if __name__ == "__main__":
    main()