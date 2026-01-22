import threading

def even_sum(arr):
    res = []
    sum = 0 

    for num in arr:
        if num % 2 == 0:
            res.append(num)

    for even_no in res:
        sum = sum + even_no

    print(f"The sum of even number from the list is : {sum}")

    
def odd_sum(arr):
    res = []
    sum = 0

    for num in arr:
        if num % 2 != 0:
            res.append(num)

    for odd_no in res:
        sum = sum + odd_no

    print(f"The sum of all odd numbers from the list is :{sum}")

    
def main():
    data = []

    elements = int(input("Enter number of elements :"))

    print("Enter numbers :")
    for i in range(elements):
        data.append(int(input()))

    Even_list = threading.Thread(target=even_sum,args=[data,])
    Odd_list = threading.Thread(target=odd_sum,args=[data,])

    Even_list.start()
    Odd_list.start()

    Even_list.join()
    Odd_list.join()

if __name__ == "__main__":
    main()