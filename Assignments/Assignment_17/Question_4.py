def sum_factor(No):
    result = 0 

    for i in range(1,No):

        if No % i == 0:

            result = result + i 

    return result

def main():
    Res = 0 

    num = int(input("Enter the number :"))

    Res = sum_factor(num)

    print(f"The sum of factors of {num} is :",Res)

if __name__ == "__main__":
    main()