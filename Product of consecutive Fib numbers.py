def productFib(prod):
    # your code
    lst = [0, 1, 1]
    if prod==1:
        return [1,1,True]
    if prod == 0:
        return [0, 1, True]
    while True:
        if lst[-1]*(lst[-1]+lst[-2])==prod:
            lst.append(lst[-1]+lst[-2])
            return [lst[-2],lst[-1],True]
        elif lst[-1]*(lst[-1]+lst[-2])>prod:
            lst.append(lst[-1]+lst[-2])
            return [lst[-2],lst[-1],False]
        else:
            lst.append(lst[-1]+lst[-2])
