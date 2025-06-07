Finito = False
s = input("Inserisci una stringa: ")
n = 0
while not Finito:
    
    n = n+1
    if s.count('a') and s.count('c') == 1:
           Finito = True
           print(n)        
    else:
        s = input("Inserisci una stringa: ")
