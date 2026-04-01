def find_min(arr):
    mn = arr[0]
    mn_id = 0
    for i in range(1, len(arr)):
        if mn > arr[i]:
            mn = arr[i]
            mn_id = i
    return mn_id

def sel_sort(arr):
    s_arr = []
    for i in range(len(arr)):
        id = find_min(arr)
        s_arr.append(arr.pop(id))
    return s_arr

print(sel_sort([5, 3, 6, 2, 10]))