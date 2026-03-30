def main1():
    k = int(input())
    s = input()
    m = 0
    for i in range(len(s)):
        mst = k
        el = s[i]
        t = i + 1
        c = 1
        while mst != 0 and t <= len(s)-1:
            if s[t] != el:
                mst -= 1
            c += 1
            t += 1
        while t <= len(s)-1:
            if s[t] == el:
                t += 1
                c += 1
            else:
                break
        if c > m:
            m = c
    print(m)

def main():
    k = int(input())
    s = input()
    mx_ch = 0
    l = 0
    count = {}
    res = 0
    for i in range(len(s)):
        el = s[i]
        if el in count:
            count[el] += 1
        else:
            count[el] = 1

        if mx_ch < count[el]:
            mx_ch = count[el]

        while i-l+1 - mx_ch > k:
            lch = s[l]
            count[lch] -= 1
            l += 1
        
        if (i - l + 1) > res:
            res = i - l + 1
    print(res)

if __name__ == "__main__":
    main()