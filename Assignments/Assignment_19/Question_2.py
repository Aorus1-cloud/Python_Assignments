def main():
    result = 0

    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    mult = lambda a,b : a * b

    result = mult(num1,num2)

    print(f"The product of {num1} and {num2} is : {result}")
    
if __name__ == "__main__":
    main()