def main2():
    n, m = list(map(int, input().split()))
    dic = {}
    for j in range(n):
        a, b = list(map(int, input().split()))
        for i in range(a, b+1):
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    st = ""
    for el in list(map(int, input().split())):
        if el in dic:
            st += str(dic[el]) + " "
        else:
            st += "0 "
    
    print(st)


def main():
    n = int(input().split()[0])
    start = []
    end = []
    for j in range(n):
        a, b = list(map(int, input().split()))
        if a > b:
            a, b = b, a
        start.append(a)
        end.append(b)
    start.sort()
    end.sort()
    res = []
    for el in list(map(int, input().split())):
        st = sum(1 for x in start if x <= el)
        ed = sum(1 for x in end if x < el)
        res.append(st-ed)
    print(*res)


if __name__ == '__main__':
    main()