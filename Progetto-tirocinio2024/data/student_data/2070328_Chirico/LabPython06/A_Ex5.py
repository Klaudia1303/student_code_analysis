s = input('inserisci una stringa = ')

rip_1 = 0
rip_2 = 0

for i in s:
    for j in s:
        if i == j:
            rip_1 = rip_1+1
            if rip_1 >= rip_2:
                rip_2 = rip_1
                x = i
        else:
            rip_1 = 0

print(x, rip_2)
            
            
            
    
