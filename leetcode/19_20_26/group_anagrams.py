def group(strs:list[str]) -> list[list[str]]:
    d = {}
    for st in strs:
        k = tuple(sorted(st))
        if k not in d:
            d[k] = [st]
        else:
            x = d[k]
            x.append(st)
            d[k] = x
    return list(d.values())

strs = ["f"]
group(strs)