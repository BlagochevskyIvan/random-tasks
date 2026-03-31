def search(list, el):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == el:
            return mid
        if guess > el:
            high = mid -1
        else:
            low = mid + 1

    return None

lst = [1, 3, 6, 8, 9]
print(search(lst, 8))