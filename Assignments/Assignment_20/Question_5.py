import threading
def count_50():
    data = list(range(1,51))

    for num in data:
        print(num,end=",")
    
    print("")
    
def reverse_50():
    data = list(range(50,0,-1))

    for num in data:
        print(num,end=",")
    
    print("")

def main():

    Thread1 = threading.Thread(target=count_50)
    Thread2 = threading.Thread(target=reverse_50)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

    
if __name__ == "__main__":
    main()