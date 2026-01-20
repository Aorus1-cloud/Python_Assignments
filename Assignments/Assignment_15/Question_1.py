def main():
    result = []
    Data = []

    print("Enter 10 numbers :")
    for i in range(10):
        x = int(input())
        Data.append(x)

    result = list(map(lambda x : x * x,Data))

    print("The square of given numbers are :")
    print(result)

if __name__ == "__main__":
    main()
