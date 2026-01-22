import threading

def even():
    data = []
    i = 2
    while(len(data) <= 10):
        if i % 2 == 0:
            data.append(i)
        
        i = i + 1
    
    print("Even Numbers :",data)

def odd():
    data = []
    i = 1
    while(len(data) <= 10):
        if i % 2 != 0:
            data.append(i)
        
        i = i + 1

    print("Odd Numbers :",data)
    
def main():
    Even = threading.Thread(target=even)
    Odd = threading.Thread(target=odd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()