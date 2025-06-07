hh=int(input('inserire le ore   '))
mm=int(input('inserire i minuti   '))
ss=int(input('inserire i secondi   '))
if hh > 0:
    mm += hh*60
if mm > 0:
    ss += mm*60
print('i secondi totatli sono :  ',ss)
    
