def cakes(rec, ing):
    try:
        res = []

        if len(rec)> len(ing):
            return 0

        else:
            for i in rec:
                res.append(ing[i]//rec[i])


            return min(res)
    except KeyError:
        return 0
