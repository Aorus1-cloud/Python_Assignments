def main():
    res = 0 
    Data = []

    print("Enter 5 numbers :")
    for i in range(5):
        x = int(input())
        Data.append(x)

    res = len(list(filter(lambda x :x % 2 == 0 ,Data)))

    print("The count of even number are :",res)
    
if __name__ == "__main__":
    main()