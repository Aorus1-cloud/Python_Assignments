def frequency(arr,num):
    count = 0
    for i in range(len(arr)):
        if int(arr[i]) == num:
            count += 1
    
    return count

def main():
    data = []
    Res = 0

    count = int(input("Enter Number of elements :"))

    print("Enter the number :")
    for i in range(count):
        data.append(int(input()))
    
    number = int(input("Element to search :"))

    Res = frequency(arr=data,num=number)

    print("The frequency of this number is :",Res)



if __name__ == "__main__":
    main()