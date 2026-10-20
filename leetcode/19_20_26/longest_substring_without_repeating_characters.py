def is_unique(s: str) -> bool:
    return len(s) == len(set(s))

def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    mx = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        mx = max(mx, right-left+1)
    return mx

    # более медленный вариант решения
    # cur_s = ""
    # mx = 0

    # for elem in s:
    #     cur_s += elem
        
    #     while not is_unique(cur_s):
    #         s = s[1:]
    #     mx = max(mx, len(cur_s))
    # return mx

print(length_of_longest_substring("abcabcbb"))  #3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3