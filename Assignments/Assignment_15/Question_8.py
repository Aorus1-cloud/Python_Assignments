def main():
    res = []
    Data = []

    print("Enter 5 Numbers below:")
    for i in range(5):
        x = int(input())
        Data.append(x)
    
    res = list(filter(lambda x : x % 3 == 0 and x % 5 == 0,Data))

    print("The number divisible by both 3 and 5 are :",res)

if __name__ == "__main__":
    main()