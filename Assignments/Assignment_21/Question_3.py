import threading

Shared_variable = 0
lock = threading.Lock()

def increment(num):
    global Shared_variable

    for i in range(num):
        # with lock:
        Shared_variable = Shared_variable + 1

def main():
    count = 0

    count = int(input("Enter number of iterations :"))

    t1 = threading.Thread(target=increment,args=(count,))
    t2 = threading.Thread(target=increment,args=(count,))
    t3 = threading.Thread(target=increment,args=(count,))


    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("The value of shared variable after iterations :",Shared_variable)

if __name__ == "__main__":
    main()