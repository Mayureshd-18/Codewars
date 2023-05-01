import math
def convert_fracts(lst):
    dnoms = []
    for i in lst:
        dnoms.append(i[1])
        
    lcm = math.lcm(*dnoms)
    
#     print("lcm is",lcm)
    
    for i in range(len(lst)):
        lst[i] = [lst[i][0]*(lcm//lst[i][1]), lcm]
        
    return lst
        
