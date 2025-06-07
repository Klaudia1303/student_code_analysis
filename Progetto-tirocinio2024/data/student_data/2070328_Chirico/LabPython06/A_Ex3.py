ott = ''


for i in range (1,8):
    for j in range (1,8):
        n = i*j
        ott = str(n//8)+str(n%8)
        print(ott, end= ' ')
    print()
        
    
