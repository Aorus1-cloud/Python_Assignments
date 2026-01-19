div_by_5 = lambda x : True if x % 5 == 0 else False

def main():
    result = False

    num = int(input("Enter the number :"))

    result = div_by_5(num)

    if result:
        print("The number is divisible by 5")
    else :
        print("The number isn't divisble by 5")

if __name__ == "__main__":
    main()