def main():
    d1 = {}
    n = int(input())
    for i in range(n):
        pr = list(map(str, input().split()))
        d1[pr[0]] = pr[1]
        d1[pr[1]] = pr[0]
    sl = input()
    print(d1[sl])

if __name__ == '__main__':
    main()