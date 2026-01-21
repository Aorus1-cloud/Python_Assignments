def factorial(No):
    result = 1

    for i in range(1,No+1):
        result = result * i
    
    return result 

def main():
    Res = 0 

    num = int(input("Enter the number :"))

    Res = factorial(num)

    print(f"The factorial of {num} is",Res)

if __name__ == "__main__":
    main()