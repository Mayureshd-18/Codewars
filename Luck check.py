def luck_check(s):
    n = len(s)
    if n==0:
        raise Exception("Empty string not allowed")
    leftsum,rsum = 0,0
    i = 0

    while i<n//2:
        try:
            leftsum+=int(s[i])
            i+=1
        except:
            raise TypeError("Only integers are allowed")

    while i<n:
        try:
            rsum+=int(s[i])
            i+=1
        except:
            raise TypeError("Only integers are allowed")
    if n%2!=0:
        rsum-=int(s[n//2])
    return (leftsum==rsum)
