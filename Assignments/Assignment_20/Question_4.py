import threading

def small(text):
    result = []

    print("Thread Id =",threading.get_ident())
    print("Thread Name =",threading.current_thread().name)
    
    for char in text:
        if char == char.lower() and not char.isdigit():
            result.append(char)
    
    # print(result)    
    print("The Small alphabets are :",len(result))

def capital(text):
    result = []

    print("Thread Id =",threading.get_ident())
    print("Thread Name =",threading.current_thread().name)

    for char in text:
        if char == char.upper() and not char.isdigit():
            result.append(char)
        
    # print(result)
    print("The Capital letters are :",len(result))

def numbers(text):
    result = []

    print("Thread Id =",threading.get_ident())
    print("Thread Name =",threading.current_thread().name)

    for char in text:
        if char.isdigit():
            result.append(char)
    
    # print(result)
    print("The integers are :",len(result))
    
def main():
    data = str()

    print("Thread Name :",threading.current_thread().name)
    print("Thread id :",threading.get_ident())

    data = input("Enter the string :")

    Small = threading.Thread(target=small,args=[data,])
    Capital = threading.Thread(target=capital,args=[data,])
    Digits = threading.Thread(target=numbers,args=[data,])

    Small.start()
    Capital.start()
    Digits.start()
    
    Small.join()
    Capital.join()
    Digits.join()

if __name__ == "__main__":
    main()