n = int(input("Inserisci un valore che rappresenta una temperatura: "))
c = input("Inserisci un carattere tra F e C: ")
C = int

if c == 'C':
    if n <= 0:
       print("solida")
    if n > 0 and n < 100:
        print("liquida")
    if n >= 100:
        print("gassosa")

        
if c == 'F':
        if n < 32 or n == 32:
            print("solida") 
        if n > 32 and n < 212:            
            print("liquida")
        if n >= 212:    
            print("gassosa")
