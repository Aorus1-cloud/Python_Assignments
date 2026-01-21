def add_list(No):
    result = 0 

    for num in No:
        result = result + int(num)

    return result

def main():
    Res = 0
    Data = []

    count = int(input("Enter Number of elements :"))

    print("Enter the numbers :")
    for i in range(count):
        Data.append(int(input()))

    Res = add_list(Data)

    print(f"The addition is : {Res}")

if __name__ == "__main__":
    main()