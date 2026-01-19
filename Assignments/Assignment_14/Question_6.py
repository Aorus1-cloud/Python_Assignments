odd = lambda x : True if x % 2 != 0 else False

def main():
    result = False

    num = int(input("Enter the number :"))

    result = odd(num)

    if result:
        print("The number is odd")
    
    else:
        print("The number is not odd")

if __name__ == "__main__":
    main() 
