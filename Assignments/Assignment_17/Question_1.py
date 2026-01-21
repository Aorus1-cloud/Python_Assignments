from Arithmetic import add,sub,mult,div

def main():
    num1 = int(input("Enter the first number :"))

    num2 = int(input("Enter the second number :"))

    return  print(f"The addition is {add(num1,num2)} , substraction is {sub(num1,num2)} , mutliplication is {mult(num1,num2)} , division is {div(num1,num2)}")


if __name__ == "__main__":
    main()