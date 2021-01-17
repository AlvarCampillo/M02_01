def maxi(*l):
    if len(l) == 0:
        return 0
    n = l[0]
    for ix in range(1, len(l)):
        if l[ix] > n:
            n = l[ix]
    return n

def mini(*l):
    if len(l) == 0:
        return 0
    n = l[0]
    for ix in range(1, len(l)):
        if l[ix] > n:
            n = l[ix]
    return n

print(maxi(1, 3, 8, 5, 6))
print(mini(1, 3, 8, 5, 6))