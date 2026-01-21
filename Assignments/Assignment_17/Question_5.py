def prime(No):
    result = False

    for i in range(2,No):
        if No % i == 0 and i != No:
            return False
        
        else:
            return True

def main():
    Res = False

    num = int(input("Enter the number :"))

    Res = prime(num)

    if Res:
        print("The number is prime")
    
    else:
        print("The number is not prime")

if __name__ == "__main__":
    main()