def main():
    s = list(map(int, input().split()))
    s.sort()
    sp = [s[0], s[1], s[-1], s[-2]]
    print(sp)


if __name__ == '__main__':
    main()