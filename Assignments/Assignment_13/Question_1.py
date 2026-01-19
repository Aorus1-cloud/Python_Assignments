def area(length,breadth):
    result = 0 

    result = length * breadth

    return result

def main():
    Res = 0 

    num1 = int(input("Enter First Number :"))
    num2 = int(input("Enter second Number :"))

    Res = area(num1,num2)

    print("The area is :",Res)

if __name__ == "__main__":
    main()