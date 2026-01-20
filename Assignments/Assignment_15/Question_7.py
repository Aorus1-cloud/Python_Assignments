def main():
    res = []
    Data = ["Hello_u","Welcome","you","greeting","me","sorry"]

    res = list(filter(lambda x : len(x) > 5,Data))

    print("The list with string greater than 5 :",res)

if __name__ == "__main__":
    main()
