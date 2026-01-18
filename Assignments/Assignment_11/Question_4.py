def reverse(No):
    return No[::-1]

def main():
    result = None

    number = input("Enter the number :").strip()

    result = reverse(number)

    print(result)

if __name__ == "__main__":
    main()