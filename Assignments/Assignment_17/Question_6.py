def pattern(no):


    # for i in range(no):
    #     print("*" * (no - i))     # Chatgpt

    num = no
    for i in range(no):

        for j in range(num):

            print("*",end="")
        print("")

        num = num - 1

def main():
    num = int(input("Enter the number :"))

    pattern(num)

if __name__ == "__main__":
    main()