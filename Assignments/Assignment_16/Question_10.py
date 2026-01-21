def word_len(text):
    return len(text)

def main():
    word = str()
    length = 0

    word = input("Enter the text :")

    length = word_len(word)

    print(length)

if __name__ == "__main__":
    main()
