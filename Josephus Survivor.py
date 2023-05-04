def josephus_survivor(n,k):
    i = 1
    ans = 0
    while(i <= n):

        ans = (ans + k) % i
        i += 1

    return ans + 1
