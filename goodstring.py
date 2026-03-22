def main():
    n = int(input())
    pr = int(input())
    c = 0
    for i in range(n - 1):
        sl = int(input())
        if sl >= pr:
            c += pr
        else:
            c += sl
        pr = sl
    print(c)


if __name__ == '__main__':
    main()