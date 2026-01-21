def stars(No):
    for i in range(No):
        print("*",end="")

def main():
    num = int(input("Enter the number :"))
    
    stars(num)

if __name__ == "__main__":
    main()