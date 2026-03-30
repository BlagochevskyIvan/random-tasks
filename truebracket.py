def main1(): #первый вариант, но довольно долгий
    n = str(input())
    while '{}' in n or '()' in n or '[]' in n:
        n = n.replace('()', '')
        n = n.replace('[]', '')
        n = n.replace('{}', '')
    if n == '':
        print("yes")
        return 0
    else:
        print("no")
        return 0
    
def main(): #метод через словарь и один проход строки
    n = input()
    dic = {")": "(", "]": "[", "}": "{"}
    arr = []
    for el in n:
        if el in "([{":
            arr.append(el)
        elif len(arr) == 0 or arr[-1] != dic[el]:
            print("no")
            return 0
        else:
            arr.pop()
    if len(arr) == 0:
        print("yes")
    else:
        print("no")
    return 0

    
if __name__ == "__main__":
    main()