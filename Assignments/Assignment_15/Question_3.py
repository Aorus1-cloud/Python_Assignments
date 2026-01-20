def main():
    result = []
    Data = []

    print("Enter 5 numbers :")
    for i in range(5):
        x= int(input())
        Data.append(x)
    
    result = list(filter(lambda x : x % 2 != 0,Data))

    print("Below are the odd numbers: ")
    print(result)

if __name__ == "__main__":
    main()
