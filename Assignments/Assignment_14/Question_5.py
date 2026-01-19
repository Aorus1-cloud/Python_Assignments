even = lambda x : True if x % 2 == 0 else False 

def main():
    result = False

    num = int(input("Enter the number :"))

    result = even(num)

    if result:
        print("Number is even")
    else :
        print("Number is not even")

if __name__ == "__main__":
    main()