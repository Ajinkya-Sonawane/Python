if __name__ == '__main__':
    s = input()
    print(any(ch.isalnum() for ch in s))
    print(any(ch.isalpha() for ch in s))
    print(any(ch.isdigit() for ch in s))
    print(any(ch.islower() for ch in s))
    print(any(ch.isupper() for ch in s))
