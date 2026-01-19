smaller = lambda x,y: x if x < y else y 

def main():
    result = 0

    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    result = smaller(x=num1 ,y=num2)

    print(f"{result} is the smaller amongs them")

if __name__ == "__main__":
    main()