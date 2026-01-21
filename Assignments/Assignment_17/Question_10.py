def length(No):
    result = 0

    for num in No:
        result = result + int(num)
    
    return result

def main():
    Res = 0 

    num = input("Enter the number :")

    Res = length(num)

    print(f"The length of {num} is {Res}")


if __name__ == "__main__":
    main()