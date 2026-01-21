def Max(No):
    result = 0

    for i in range(len(No)-1):

        if No[i] > No[i + 1]:
            result = No[i]
        else:
            result = No[i+1]

    return result

def main():
    data = []
    Res = 0

    count = int(input("Enter Number of elements :"))

    print("Enter the number :")
    for i in range(count):
        data.append(int(input()))

    Res = Max(data)

    print("The largest number in the list is :",Res)

if __name__ == "__main__":
    main()