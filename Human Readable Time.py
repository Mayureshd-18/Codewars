def make_readable(sec1):
    hh,mm,ss = 0,0,0

    hh = sec1//3600
    sec1 -= hh*3600
    
    mm = sec1//60
    sec1-= mm*60
    
    ss = sec1

    return f"{hh:02d}:{mm:02d}:{ss:02d}"
