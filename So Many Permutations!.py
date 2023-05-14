from itertools import permutations as permu
def permutations(a):
    permutation = [''.join(p) for p in permu(a)]
    return list(set(permutation))
