b= int(input('inserire la basa del triangolo: '))

conta=0

for c in range(1,b+1,2):
    l= b//2-(int(conta))
    dis= '*'*c
    conta=conta+1
    spazio=' '*int(l)
    
    print(str(spazio)+str(dis))


