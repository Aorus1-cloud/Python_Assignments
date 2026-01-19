def binary(No):
    res = []

    while(No >= 1):
        res.append(No%2)
        No = No // 2

    return(res[::-1])

def main():
    Res = 0

    num = int(input("Enter the number :"))

    Res = binary(num)
    

    print(f"The binary equivalent of {num} is :")
    for no in Res:
        print(no,end="")

if __name__ == "__main__":
    main()