k = int(input().split()[1])
c = 0
for elem in list(map(int, input().split())):
    if elem >= k:
        c += 1

print(c)