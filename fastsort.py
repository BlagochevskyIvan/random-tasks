def fastsort(arr):
    if len(arr) < 2:
        return arr
    else:
        op = arr[0]
        left = []
        right = []
        for el in arr[1:]:
            left.append(el) if el <= op else right.append(el)
        return fastsort(left) + [op] + fastsort(right)
    
print(fastsort([0, 4, 2, 5, 7, 79, 20, 4, 49, 485, 592, 3, 5, 9]))