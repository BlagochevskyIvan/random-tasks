def main():
    n = list(input())
    sl = {str(i+1): chr(97+i) for i in range(26)}
    st = ''
    skip = 0
    for i in range(len(n)):
        if skip != 0:
            skip -= 1
            continue

        if i + 2 < len(n) and n[i+2] == "#":
            st += sl[str(n[i]) + str(n[i+1])]
            skip += 2
        else:
            st += sl[n[i]]
    print(st)

if __name__ == '__main__':
    main()