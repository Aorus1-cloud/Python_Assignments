import threading

def max(arr):
    result = 0 

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            result = arr[i]
        else:
            result = arr[i + 1]
        
    print("The maximum amongst the numbers is :",result)
        
def min(arr):
    result = 0

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            result = arr[i]
        else:
            result = arr[i + 1]

    print("The minimum amongst the numbers is :",result)

def main():
    data = []
    num = 0 

    num = int(input("Enter the number of elements :"))

    print("Enter the numbers :")
    for i in range(num):
        data.append(int(input()))

    Max = threading.Thread(target=max,args=(data,))
    Min = threading.Thread(target=min,args=(data,))

    Max.start()
    Min.start()

    Max.join()
    Min.join()

if __name__ == "__main__":
    main()