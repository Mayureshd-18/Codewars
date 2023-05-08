def middle_permutation(string):
    res = []
    def toString(List):
        return ''.join(List)

    def permute(a, l, r):
        if l == r:
            res.append(toString(a))
        else:
            for i in range(l, r):
                a[l], a[i] = a[i], a[l]
                permute(a, l + 1, r)
                a[l], a[i] = a[i], a[l]  # backtrack


    n = len(string)
    a = list(string)

    permute(a, 0, n)
    res.sort()
    l = len(res)
    return res[(l//2) - 1 ] if l%2==0 else res[l//2]

