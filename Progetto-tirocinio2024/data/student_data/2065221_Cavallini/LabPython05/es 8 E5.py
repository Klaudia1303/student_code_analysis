base = int(input('inseisci la base del triangolo: '))
spazio = 0
x = ' '
for i in range(1,base+1,2):
    spazi = x*(base//2-spazio)
    spazio+=1
    asterisco = i*'*'
    print(spazi+asterisco)
    
    
