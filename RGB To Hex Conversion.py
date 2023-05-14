def rgb(a,b,c):
    x = [a,b,c]
    for i in range(len(x)):
        if x[i] < 0:
            x[i] = 0
        elif x[i] > 255:
            x[i] = 255
    res = []
    for i in x:
        if i==0:
            res.append("00")

        else:

            res.append((hex(i).lstrip("0x").rstrip("L").upper()))
    # print(res)
    for i in range(len(res)):
#         try:
#             if 0<int(res[i])<9:
#                 res[i] = f"0{str(res[i])}"
#         except:
#             pass
          if len(res[i]) == 1:
            res[i] = f"0{res[i]}"

    f = "".join(res)
    return f
