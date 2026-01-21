def pattern(No):

    for i in range(No):

        for j in range(No):

            print("*",end="")
            
        print("")

def main():
    num = 0

    num = int(input("Enter the number :"))

    pattern(num)


if __name__ == "__main__":
    main()