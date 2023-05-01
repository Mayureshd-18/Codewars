def comp(array1, array2):
    if (array1 == [] and array2==[]) or (array1==None and array2==None):
        return True
    elif array1 is not None and array2 is not None:

        array1 = sorted(list(map(lambda x: x*x, array1)))
        array2.sort()
        return array1 == array2
    else:
        return False
