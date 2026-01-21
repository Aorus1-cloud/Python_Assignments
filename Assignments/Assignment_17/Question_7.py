def num_pattern(No):
    for i in range(No):
        for j in range(1,No+1):
            print(j,end="")
        print("")

def main():
    num = 0

    num = int(input("Enter the number :"))

    num_pattern(num)

if __name__ == "__main__":
    main()