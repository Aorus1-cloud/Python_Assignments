def Add(No1,No2):
    return No1+No2

def main():
    result = 0

    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    result = Add(num1,num2)

    print("The addition of both numbers is :",result)

if __name__ =="__main__":
    main()