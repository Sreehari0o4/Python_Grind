def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):
    short=''
    for i in word:
        if i.lower() not in ['a','e', 'i', 'o', 'u']:
            short += i
    return short


if __name__ == "__main__":
    main()