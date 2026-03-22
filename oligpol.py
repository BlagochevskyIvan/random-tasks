def main():
    n = int(input())
    arr = list(map(int, input().split()))
    pr = [0] * n
    pr[0] = arr[0]
    res = [0] * n

    for i in range(1, n):
        pr[i] = pr[i-1] + arr[i]

    for i in range(n-2, -1, -1):
        if pr[i] > arr[i+1]:
            res[i] = 1
    res[n-1] = 1
    for r in res:
        print(r)
        
if __name__ == '__main__':
    main()