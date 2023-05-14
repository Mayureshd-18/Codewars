def format_duration(n):
    yrs = n//(365*24*60*60)
    if yrs>0:
        n-= (yrs*365*24*60*60)

    days = n//(24*60*60)
    if days>0:
        n-=(days*24*60*60)

    hrs = n//(60*60)
    if hrs>0:
        n-=(hrs*60*60)

    mins = n//60
    if mins>0:
        n-=mins*60

    secs = 0
    if n>0:
        secs = n


    lst1 = (yrs,days,hrs,mins,secs)

    ctr = 0
    for j in lst1:
        if j>0:
            ctr+=1

    lst2 = ("years", "days", "hours","minutes", "seconds")
    lst3 = ("year","day","hour","minute","second")

    # mydict = {yrs:"years", days:"days", hrs:"hours", mins:"minutes", secs:"seconds"}
    # print(mydict)
    res = ""

    for i in range(len(lst1)):
        if lst1[i] > 0:

            if lst1[i]==1:
                res+=f", {lst1[i]} {lst3[i]}"

            else:
                res+=f", {lst1[i]} {lst2[i]}"
    try:
        if res[0]==",":
            res = res[1:]
    except:
        return "now"


    removal = ","
    replacement = "dna "

    newstr = res[::-1].replace(removal, replacement, 1)[::-1]
#     print ("mystr:", res)
    return(newstr.strip())
