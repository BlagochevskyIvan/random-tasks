s = input().strip()
n = len(s)
num_a = n - len(s.rstrip("a"))
for prln in range(n, n - num_a - 1, -1):
    i = s[:prln]
    if i == i[::-1]:
        print("Yes")
        break
else:
    print("No")

    