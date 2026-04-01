def arrsum(arr):
    if arr == []:
        return 0
    else:
        return arr.pop(0) + arrsum(arr)
    
def arrct(arr):
    if arr == []:
        return 0
    else:
        arr.pop(0)
        return 1 + arrct(arr)
    
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])
    
def arrmx(arr):
    #простой случай - конкретное число
    #идём по элементам и сравниваем первый со следующим и выводим максимум
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    pr_mx = arrmx(arr[1:])
    return pr_mx if arr[0] < pr_mx else arr[0]

        
    
print(arrsum([1, 2, 3]))
    
print(arrct([1, 2, 3]))

print(arrmx([1, 7, 3, 4, 2, 2, 1, 5, 2, 2]))