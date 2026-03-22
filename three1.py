def main2():
    n = int(input())
    def c(b):
        if '111' in b:
            return 0
        elif len(b) < n:
            return c(b + '1') + c(b + '0')
        else:
            return 1

    print(c(''))

def main():
    n = int(input())
    if n == 0:
        print(1)
        return 0
    elif n == 1:
        print(2)
        return 0
    elif n == 2:
        print(4)
        return 0

    x, y, z = 1, 2, 4
    for i in range(3, n+1):
        x, y, z = y, z, x + y + z
    
    print(z)

if __name__ == '__main__':
    main()