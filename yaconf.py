all = int(input().split()[0])
zab = list(map(int, input().split()))
zap = list(map(int, input().split()))

for i in zap[:]:
    if i in zab:
        zab.remove(i)
        zap.remove(i)

for i in zap:
    if i - 1 in zab:
        zab.remove(i - 1)
    elif i + 1 in zab:
        zab.remove(i + 1)

print(all - len(zab))