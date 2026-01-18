def Factorial(No):
    Res = 1

    for i in range(1,No+1):
        Res = Res * i 
    
    return Res

def main():
    Result = 0 
    
    Number = int(input("Enter the Number : "))

    Result = Factorial(Number)

    print(f"The Factorial of {Number} is : ",Result)

if __name__ == "__main__":
    main()